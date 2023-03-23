
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def add_node(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            
            while True:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
                        
    def print_leaves(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.data, end=' ')
            self.print_leaves(node.left)
            self.print_leaves(node.right)
            
tree = BinaryTree()
tree.add_node(6)
tree.add_node(2)
tree.add_node(8)
tree.add_node(1)
tree.add_node(4)
tree.add_node(3)
tree.add_node(5)
tree.add_node(7)
tree.add_node(9)

print('Leaves of the binary tree:')
tree.print_leaves(tree.root)
