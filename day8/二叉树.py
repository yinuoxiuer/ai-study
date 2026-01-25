class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue = []

    def level_build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if not self.help_queue[0].lchild:
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node
                self.help_queue.pop(0)
    def pre_order(self,current_node: Node):
        print(current_node.elem)
        if current_node.lchild:
            self.pre_order(current_node.lchild)
            if current_node.rchild:
                self.pre_order(current_node.rchild)
    def in_order(self,current_node: Node):
        if  current_node:
            self.in_order(current_node.lchild)
            print(current_node.elem)
            self.in_order(current_node.rchild)
    def level_order(self,current_node: Node):
        help_queue = []
        if  current_node:
            help_queue.append(current_node)
        while  help_queue:
            print(help_queue[0].elem)
            out_node=help_queue.pop(0)
            if out_node.lchild:
                help_queue.append(out_node.lchild)
            if out_node.rchild:
                help_queue.append(out_node.rchild)





if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.level_build_tree(new_node)
    tree.pre_order(tree.root)
    tree.in_order(tree.root)
    tree.level_order(tree.root)







