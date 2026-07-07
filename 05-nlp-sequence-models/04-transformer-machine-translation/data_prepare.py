"""Download and unpack the Multi30k German-English files used by this unit.

The Transformer notebooks expect plain text files under `wmt16/` with names like
`train.de`, `train.en`, `val.de`, and `test.en`. This helper downloads the gzip
files from the public Multi30k repository and writes those expected filenames.
"""

import gzip
import os
import urllib.request


DATA_DIR = "wmt16"
URLS = {
    "train.de": "https://raw.githubusercontent.com/multi30k/dataset/master/data/task1/raw/train.de.gz",
    "train.en": "https://raw.githubusercontent.com/multi30k/dataset/master/data/task1/raw/train.en.gz",
    "val.de": "https://raw.githubusercontent.com/multi30k/dataset/master/data/task1/raw/val.de.gz",
    "val.en": "https://raw.githubusercontent.com/multi30k/dataset/master/data/task1/raw/val.en.gz",
    "test.de": "https://raw.githubusercontent.com/multi30k/dataset/master/data/task1/raw/test_2016_flickr.de.gz",
    "test.en": "https://raw.githubusercontent.com/multi30k/dataset/master/data/task1/raw/test_2016_flickr.en.gz",
}


def download_and_unpack(filename: str, url: str) -> None:
    """Download one gzip file and save the decompressed text into DATA_DIR."""
    print(f"Downloading and unpacking {filename} ...")
    try:
        response = urllib.request.urlopen(url)
        with open(os.path.join(DATA_DIR, filename), "wb") as out_file:
            out_file.write(gzip.decompress(response.read()))
        print(f"Done: {filename}")
    except Exception as exc:
        print(f"Failed to download {filename}: {exc}")


def main() -> None:
    """Create the data directory and fetch all train/val/test splits."""
    os.makedirs(DATA_DIR, exist_ok=True)
    for filename, url in URLS.items():
        download_and_unpack(filename, url)
    print("All Multi30k files are ready under wmt16/.")


if __name__ == "__main__":
    main()
