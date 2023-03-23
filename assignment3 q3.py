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
                        
    def pre_order(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)
            
    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.data, end=' ')
            self.in_order(node.right)
            
    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=' ')
            
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

print('Pre-order traversal:')
tree.pre_order(tree.root)

print('\nIn-order traversal:')
tree.in_order(tree.root)

print('\nPost-order traversal:')
tree.post_order(tree.root)
