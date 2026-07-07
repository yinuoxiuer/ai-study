"""Standalone Transformer implementation for the machine translation study unit.

This script keeps the core pieces from the Transformer notebooks in one readable
Python module: vocabulary loading, tokenization, sinusoidal position embedding,
multi-head attention, encoder/decoder blocks, training helpers, and inference.
It is intentionally explicit so each tensor shape and mask can be traced while
reviewing the original paper implementation.
"""
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from subword_nmt.apply_bpe import BPE


def _resolve_project_root() -> Path:
    """Locate the study unit root whether the script runs from root or notebooks."""
    cwd = Path.cwd()
    if (cwd / "wmt16").exists():
        return cwd
    if (cwd.parent / "wmt16").exists():
        return cwd.parent
    return cwd


def load_vocab(vocab_path: str, threshold: int = 1):
    """Load a BPE vocabulary file and reserve the first ids for special tokens."""
    word2idx = {
        "[PAD]": 0,
        "[BOS]": 1,
        "[UNK]": 2,
        "[EOS]": 3,
    }
    idx2word = {value: key for key, value in word2idx.items()}
    index = len(idx2word)
    with open(vocab_path, "r", encoding="utf8") as file:
        for line in file.readlines():
            token, counts = line.strip().split()
            if int(counts) >= threshold:
                word2idx[token] = index
                idx2word[index] = token
                index += 1
    return word2idx, idx2word, len(word2idx)


class Tokenizer:
    """Convert token lists to padded id tensors and decode ids back to text."""
    def __init__(self, word2idx, idx2word, max_length=128, pad_idx=0, bos_idx=1, eos_idx=3, unk_idx=2):
        self.word2idx = word2idx
        self.idx2word = idx2word
        self.max_length = max_length
        self.pad_idx = pad_idx
        self.bos_idx = bos_idx
        self.eos_idx = eos_idx
        self.unk_idx = unk_idx

    def encode(self, text_list, padding_first=False, add_bos=True, add_eos=True, return_mask=False):
        max_length = min(self.max_length, add_eos + add_bos + max(len(text) for text in text_list))
        indices_list = []
        for text in text_list:
            indices = [self.word2idx.get(word, self.unk_idx) for word in text[: max_length - add_bos - add_eos]]
            if add_bos:
                indices = [self.bos_idx] + indices
            if add_eos:
                indices = indices + [self.eos_idx]
            if padding_first:
                indices = [self.pad_idx] * (max_length - len(indices)) + indices
            else:
                indices = indices + [self.pad_idx] * (max_length - len(indices))
            indices_list.append(indices)
        input_ids = torch.tensor(indices_list)
        masks = (input_ids == self.pad_idx).to(dtype=torch.int64)
        return input_ids if not return_mask else (input_ids, masks)

    def decode(self, indices_list, remove_bos=True, remove_eos=True, remove_pad=True, split=False):
        text_list = []
        for indices in indices_list:
            text = []
            for index in indices:
                word = self.idx2word.get(index, "[UNK]")
                if remove_bos and word == "[BOS]":
                    continue
                if remove_eos and word == "[EOS]":
                    break
                if remove_pad and word == "[PAD]":
                    break
                text.append(word)
            text_list.append(" ".join(text) if not split else text)
        return text_list


Tensor = torch.Tensor


@dataclass
class AttentionOutput:
    hidden_states: Tensor
    attn_scores: Tensor


@dataclass
class TransformerBlockOutput:
    hidden_states: Tensor
    self_attn_scores: Tensor
    cross_attn_scores: Optional[Tensor] = None


@dataclass
class TransformerEncoderOutput:
    last_hidden_states: Tensor
    attn_scores: List[Tensor]


@dataclass
class TransformerDecoderOutput:
    last_hidden_states: Tensor
    self_attn_scores: List[Tensor]
    cross_attn_scores: List[Tensor]


@dataclass
class TransformerOutput:
    logits: Tensor
    encoder_last_hidden_states: Tensor
    encoder_attn_scores: List[Tensor]
    decoder_last_hidden_states: Tensor
    decoder_self_attn_scores: List[Tensor]
    decoder_cross_attn_scores: List[Tensor]
    preds: Optional[Tensor] = None


class TransformerEmbedding(nn.Module):
    """Token embedding plus fixed sinusoidal position embedding."""
    def __init__(self, config):
        super().__init__()
        self.vocab_size = config["vocab_size"]
        self.hidden_size = config["d_model"]
        self.pad_idx = config["pad_idx"]
        dropout_rate = config["dropout"]
        self.max_length = config["max_length"]

        self.word_embedding = nn.Embedding(self.vocab_size, self.hidden_size, padding_idx=self.pad_idx)
        self.pos_embedding = nn.Embedding(
            self.max_length,
            self.hidden_size,
            _weight=self.get_positional_encoding(self.max_length, self.hidden_size),
        )
        self.pos_embedding.weight.requires_grad_(False)
        self.dropout = nn.Dropout(dropout_rate)

    def get_word_embedding_weights(self):
        return self.word_embedding.weight

    @classmethod
    def get_positional_encoding(cls, max_length, hidden_size):
        pe = torch.zeros(max_length, hidden_size)
        position = torch.arange(0, max_length).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, hidden_size, 2) * -(torch.log(torch.tensor([10000.0])) / hidden_size))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        return pe

    def forward(self, input_ids):
        seq_len = input_ids.shape[1]
        if seq_len > self.max_length:
            raise ValueError(f"input sequence length should no more than {self.max_length} but got {seq_len}")
        position_ids = torch.arange(seq_len, dtype=torch.long, device=input_ids.device)
        position_ids = position_ids.unsqueeze(0).expand_as(input_ids)
        word_embeds = self.word_embedding(input_ids)
        pos_embeds = self.pos_embedding(position_ids)
        embeds = self.dropout(word_embeds + pos_embeds)
        return embeds


class MultiHeadAttention(nn.Module):
    """Scaled dot-product attention split across multiple heads."""
    def __init__(self, config):
        super().__init__()
        self.hidden_size = config["d_model"]
        self.num_heads = config["num_heads"]
        if self.hidden_size % self.num_heads != 0:
            raise ValueError("Hidden size must be divisible by num_heads")
        self.head_dim = self.hidden_size // self.num_heads

        self.Wq = nn.Linear(self.hidden_size, self.hidden_size, bias=False)
        self.Wk = nn.Linear(self.hidden_size, self.hidden_size, bias=False)
        self.Wv = nn.Linear(self.hidden_size, self.hidden_size, bias=False)
        self.Wo = nn.Linear(self.hidden_size, self.hidden_size, bias=False)

    def _split_heads(self, x: Tensor) -> Tensor:
        bs, seq_len, _ = x.shape
        x = x.view(bs, seq_len, self.num_heads, self.head_dim)
        return x.permute(0, 2, 1, 3)

    def _merge_heads(self, x: Tensor) -> Tensor:
        bs, _, seq_len, _ = x.shape
        return x.permute(0, 2, 1, 3).reshape(bs, seq_len, self.hidden_size)

    def forward(self, querys, keys, values, attn_mask=None) -> AttentionOutput:
        querys = self._split_heads(self.Wq(querys))
        keys = self._split_heads(self.Wk(keys))
        values = self._split_heads(self.Wv(values))

        # Attention scores have shape [batch, heads, query_len, key_len].
        # Masks use 1 for blocked positions and are converted to a large negative bias.
        qk_logits = torch.matmul(querys, keys.transpose(-1, -2))
        if attn_mask is not None:
            attn_mask = attn_mask[:, :, : querys.shape[-2], : keys.shape[-2]]
            qk_logits += attn_mask * -1e9
        attn_scores = F.softmax(qk_logits / (self.head_dim**0.5), dim=-1)
        embeds = torch.matmul(attn_scores, values)
        embeds = self.Wo(self._merge_heads(embeds))
        return AttentionOutput(hidden_states=embeds, attn_scores=attn_scores)


class TransformerBlock(nn.Module):
    """One encoder/decoder block: self-attention, optional cross-attention, FFN."""
    def __init__(self, config, add_cross_attention=False):
        super().__init__()
        self.hidden_size = config["d_model"]
        dropout_rate = config["dropout"]
        ffn_dim = config["dim_feedforward"]
        eps = config["layer_norm_eps"]

        self.self_atten = MultiHeadAttention(config)
        self.self_ln = nn.LayerNorm(self.hidden_size, eps=eps)
        self.self_dropout = nn.Dropout(dropout_rate)

        if add_cross_attention:
            self.cross_atten = MultiHeadAttention(config)
            self.cross_ln = nn.LayerNorm(self.hidden_size, eps=eps)
            self.cross_dropout = nn.Dropout(dropout_rate)
        else:
            self.cross_atten = None

        self.ffn = nn.Sequential(
            nn.Linear(self.hidden_size, ffn_dim),
            nn.ReLU(),
            nn.Linear(ffn_dim, self.hidden_size),
        )
        self.ffn_ln = nn.LayerNorm(self.hidden_size, eps=eps)
        self.ffn_dropout = nn.Dropout(dropout_rate)

    def forward(self, hidden_states, attn_mask=None, encoder_outputs=None, cross_attn_mask=None):
        self_atten_output = self.self_atten(hidden_states, hidden_states, hidden_states, attn_mask)
        self_embeds = self.self_ln(hidden_states + self.self_dropout(self_atten_output.hidden_states))

        cross_embeds = self_embeds
        cross_attn_scores = None
        if self.cross_atten is not None:
            if encoder_outputs is None:
                raise ValueError("encoder_outputs is required for cross-attention")
            cross_atten_output = self.cross_atten(self_embeds, encoder_outputs, encoder_outputs, cross_attn_mask)
            cross_embeds = self.cross_ln(self_embeds + self.cross_dropout(cross_atten_output.hidden_states))
            cross_attn_scores = cross_atten_output.attn_scores

        ffn_output = self.ffn(cross_embeds)
        embeds = self.ffn_ln(cross_embeds + self.ffn_dropout(ffn_output))

        return TransformerBlockOutput(
            hidden_states=embeds,
            self_attn_scores=self_atten_output.attn_scores,
            cross_attn_scores=cross_attn_scores,
        )


class TransformerEncoder(nn.Module):
    """Stack encoder blocks and return hidden states plus attention maps."""
    def __init__(self, config):
        super().__init__()
        self.num_layers = config["num_encoder_layers"]
        self.layers = nn.ModuleList([TransformerBlock(config) for _ in range(self.num_layers)])

    def forward(self, encoder_inputs_embeds, attn_mask=None) -> TransformerEncoderOutput:
        attn_scores = []
        embeds = encoder_inputs_embeds
        for layer in self.layers:
            block_outputs = layer(embeds, attn_mask=attn_mask)
            embeds = block_outputs.hidden_states
            attn_scores.append(block_outputs.self_attn_scores)
        return TransformerEncoderOutput(last_hidden_states=embeds, attn_scores=attn_scores)


class TransformerDecoder(nn.Module):
    """Stack decoder blocks with causal self-attention and encoder cross-attention."""
    def __init__(self, config):
        super().__init__()
        self.num_layers = config["num_decoder_layers"]
        self.layers = nn.ModuleList([TransformerBlock(config, add_cross_attention=True) for _ in range(self.num_layers)])

    def forward(self, decoder_inputs_embeds, encoder_outputs, attn_mask=None, cross_attn_mask=None) -> TransformerDecoderOutput:
        self_attn_scores = []
        cross_attn_scores = []
        embeds = decoder_inputs_embeds
        for layer in self.layers:
            block_outputs = layer(
                embeds,
                attn_mask=attn_mask,
                encoder_outputs=encoder_outputs,
                cross_attn_mask=cross_attn_mask,
            )
            embeds = block_outputs.hidden_states
            self_attn_scores.append(block_outputs.self_attn_scores)
            cross_attn_scores.append(block_outputs.cross_attn_scores)
        return TransformerDecoderOutput(
            last_hidden_states=embeds,
            self_attn_scores=self_attn_scores,
            cross_attn_scores=cross_attn_scores,
        )


class TransformerModel(nn.Module):
    """Wrap embeddings, encoder, decoder, output projection, and mask creation."""
    def __init__(self, config):
        super().__init__()
        self.hidden_size = config["d_model"]
        self.num_encoder_layers = config["num_encoder_layers"]
        self.num_decoder_layers = config["num_decoder_layers"]
        self.pad_idx = config["pad_idx"]
        self.bos_idx = config["bos_idx"]
        self.eos_idx = config["eos_idx"]
        self.vocab_size = config["vocab_size"]
        self.dropout_rate = config["dropout"]
        self.max_length = config["max_length"]
        self.share = config["share_embedding"]

        self.src_embedding = TransformerEmbedding(config)
        if self.share:
            self.trg_embedding = self.src_embedding
            self.linear = lambda x: torch.matmul(x, self.trg_embedding.get_word_embedding_weights().T)
        else:
            self.trg_embedding = TransformerEmbedding(config)
            self.linear = nn.Linear(self.hidden_size, self.vocab_size)

        self.encoder = TransformerEncoder(config)
        self.decoder = TransformerDecoder(config)
        self._init_weights()

    def _init_weights(self):
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

    def generate_square_subsequent_mask(self, sz: int) -> Tensor:
        mask = (torch.triu(torch.ones(sz, sz)) == 0).transpose(-1, -2).bool()
        return mask

    def forward(self, encoder_inputs, decoder_inputs, encoder_inputs_mask=None) -> TransformerOutput:
        if encoder_inputs_mask is None:
            encoder_inputs_mask = encoder_inputs.eq(self.pad_idx)
        encoder_inputs_mask = encoder_inputs_mask.unsqueeze(1).unsqueeze(2)
        look_ahead_mask = self.generate_square_subsequent_mask(decoder_inputs.shape[1])
        look_ahead_mask = look_ahead_mask.unsqueeze(0).unsqueeze(0).to(decoder_inputs.device)

        decoder_inputs_mask = decoder_inputs.eq(self.pad_idx)
        decoder_inputs_mask = decoder_inputs_mask.unsqueeze(1).unsqueeze(2)
        decoder_inputs_mask = decoder_inputs_mask + look_ahead_mask

        encoder_inputs_embeds = self.src_embedding(encoder_inputs)
        encoder_outputs = self.encoder(encoder_inputs_embeds, encoder_inputs_mask)

        decoder_inputs_embeds = self.trg_embedding(decoder_inputs)
        decoder_outputs = self.decoder(
            decoder_inputs_embeds=decoder_inputs_embeds,
            encoder_outputs=encoder_outputs.last_hidden_states,
            attn_mask=decoder_inputs_mask,
            cross_attn_mask=encoder_inputs_mask,
        )

        logits = self.linear(decoder_outputs.last_hidden_states)
        return TransformerOutput(
            logits=logits,
            encoder_last_hidden_states=encoder_outputs.last_hidden_states,
            encoder_attn_scores=encoder_outputs.attn_scores,
            decoder_last_hidden_states=decoder_outputs.last_hidden_states,
            decoder_self_attn_scores=decoder_outputs.self_attn_scores,
            decoder_cross_attn_scores=decoder_outputs.cross_attn_scores,
        )

    @torch.no_grad()
    def infer(self, encoder_inputs, encoder_inputs_mask=None) -> TransformerOutput:
        if encoder_inputs_mask is None:
            encoder_inputs_mask = encoder_inputs.eq(self.pad_idx)
        encoder_inputs_mask = encoder_inputs_mask.unsqueeze(1).unsqueeze(2)
        look_ahead_mask = self.generate_square_subsequent_mask(self.max_length)
        look_ahead_mask = look_ahead_mask.unsqueeze(0).unsqueeze(0).to(encoder_inputs.device)

        encoder_inputs_embeds = self.src_embedding(encoder_inputs)
        encoder_outputs = self.encoder(encoder_inputs_embeds)

        decoder_inputs = torch.tensor([self.bos_idx] * encoder_inputs.shape[0]).reshape(-1, 1).long().to(encoder_inputs.device)
        for cur_len in range(1, self.max_length + 1):
            decoder_inputs_embeds = self.trg_embedding(decoder_inputs)
            decoder_outputs = self.decoder(
                decoder_inputs_embeds=decoder_inputs_embeds,
                encoder_outputs=encoder_outputs.last_hidden_states,
                attn_mask=look_ahead_mask[:, :, :cur_len, :cur_len],
            )
            logits = self.linear(decoder_outputs.last_hidden_states)
            next_token = logits.argmax(dim=-1)[:, -1:]
            decoder_inputs = torch.cat([decoder_inputs, next_token], dim=-1)
            if all((decoder_inputs == self.eos_idx).sum(dim=-1) > 0):
                break

        return TransformerOutput(
            preds=decoder_inputs[:, 1:],
            logits=logits,
            encoder_last_hidden_states=encoder_outputs.last_hidden_states,
            encoder_attn_scores=encoder_outputs.attn_scores,
            decoder_last_hidden_states=decoder_outputs.last_hidden_states,
            decoder_self_attn_scores=decoder_outputs.self_attn_scores,
            decoder_cross_attn_scores=decoder_outputs.cross_attn_scores,
        )


class BasicTokenizer:
    _pattern = re.compile(r"\w+|[^\w\s]", re.UNICODE)

    def tokenize(self, text: str):
        return self._pattern.findall(text.lower())


class BasicDetokenizer:
    _punct = re.compile(r"\s+([,.!?;:])")

    def detokenize(self, tokens):
        text = " ".join(tokens)
        return self._punct.sub(r"\\1", text)


class Translator:
    def __init__(self, model, src_tokenizer, trg_tokenizer, bpe_codes_path=None):
        if bpe_codes_path is None:
            project_root = _resolve_project_root()
            bpe_codes_path = project_root / "wmt16" / "bpe.20000"
        else:
            bpe_codes_path = Path(bpe_codes_path)
        if not bpe_codes_path.exists():
            raise FileNotFoundError(f"BPE codes not found: {bpe_codes_path}")
        with bpe_codes_path.open("r", encoding="utf8") as codes:
            self.bpe = BPE(codes)
        self.tokenizer = BasicTokenizer()
        self.detokenizer = BasicDetokenizer()
        self.model = model
        self.model.eval()
        self.src_tokenizer = src_tokenizer
        self.trg_tokenizer = trg_tokenizer
        self.pattern = re.compile(r"(@@ )|(@@ ?$)")

    def draw_attention_map(self, attn_scores, cross_attn_scores, src_words_list, trg_words_list):
        import matplotlib.pyplot as plt

        attn_scores = attn_scores[:, : len(trg_words_list), : len(trg_words_list)]
        cross_attn_scores = cross_attn_scores[:, : len(trg_words_list), : len(src_words_list)]

        trg_len = len(trg_words_list)
        src_len = len(src_words_list)

        fig = plt.figure(figsize=(10, 5), constrained_layout=True)
        grid = plt.GridSpec(trg_len, trg_len + src_len, wspace=0.1, hspace=0.1)

        self_map = fig.add_subplot(grid[:, :trg_len])
        self_map.matshow(attn_scores.mean(dim=0), cmap="viridis")
        self_map.set_yticks(range(trg_len), trg_words_list, fontsize=10)
        self_map.set_xticks(range(trg_len), ["[BOS]"] + trg_words_list[:-1], rotation=90)

        cross_map = fig.add_subplot(grid[:, trg_len:])
        cross_map.matshow(cross_attn_scores.mean(dim=0), cmap="viridis")
        cross_map.set_yticks(range(trg_len), [], fontsize=6)
        cross_map.set_xticks(range(src_len), src_words_list, rotation=90)

        plt.show()

    def draw_attention_maps(self, attn_scores, cross_attn_scores, src_words_list, trg_words_list, heads_list):
        import matplotlib.pyplot as plt

        attn_scores = attn_scores[:, : len(trg_words_list), : len(trg_words_list)]
        cross_attn_scores = cross_attn_scores[:, : len(trg_words_list), : len(src_words_list)]

        trg_len = len(trg_words_list)
        src_len = len(src_words_list)

        fig, axes = plt.subplots(2, len(heads_list), figsize=(5 * len(heads_list), 10))
        for i, heads_idx in enumerate(heads_list):
            axes[0, i].matshow(attn_scores[heads_idx], cmap="viridis")
            axes[0, i].set_yticks(range(trg_len), trg_words_list)
            axes[0, i].set_xticks(range(trg_len), ["[BOS]"] + trg_words_list[:-1], rotation=90)
            axes[0, i].set_title(f"head {heads_idx}")
            axes[1, i].matshow(cross_attn_scores[heads_idx], cmap="viridis")
            axes[1, i].set_yticks(range(trg_len), trg_words_list)
            axes[1, i].set_xticks(range(src_len), src_words_list, rotation=90)
            axes[1, i].set_title(f"head {heads_idx}")

        plt.show()

    def __call__(self, sentence_list, heads_list=None, layer_idx=-1):
        tokens_list = []
        for s in sentence_list:
            tokens = self.tokenizer.tokenize(s)
            bpe_line = self.bpe.process_line(" ".join(tokens))
            tokens_list.append(bpe_line.split())
        encoder_input, attn_mask = self.src_tokenizer.encode(tokens_list, add_bos=True, add_eos=True, return_mask=True)
        encoder_input = torch.tensor(encoder_input).to(dtype=torch.int64)
        outputs = self.model.infer(encoder_inputs=encoder_input, encoder_inputs_mask=attn_mask)

        preds = outputs.preds.numpy()
        trg_decoded = self.trg_tokenizer.decode(preds, split=True, remove_eos=False, remove_bos=False, remove_pad=False)
        src_decoded = self.src_tokenizer.decode(
            encoder_input.numpy(),
            split=True,
            remove_bos=False,
            remove_eos=False,
        )

        for attn_score, cross_attn_score, src, trg in zip(
            outputs.decoder_self_attn_scores[layer_idx],
            outputs.decoder_cross_attn_scores[layer_idx],
            src_decoded,
            trg_decoded,
        ):
            if heads_list is None:
                self.draw_attention_map(attn_score, cross_attn_score, src, trg)
            else:
                self.draw_attention_maps(attn_score, cross_attn_score, src, trg, heads_list=heads_list)

        return [
            self.detokenizer.detokenize(self.pattern.sub("", s).split())
            for s in self.trg_tokenizer.decode(preds)
        ]


def load_checkpoint(model, ckpt_path, map_location="cpu"):
    state_dict = torch.load(ckpt_path, map_location=map_location)
    model.load_state_dict(state_dict)
    return model



