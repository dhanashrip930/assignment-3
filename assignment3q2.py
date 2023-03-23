#Find height of a given tree

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
                        
    def get_height(self, node):
        if node is None:
            return 0
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        
        return max(left_height, right_height) + 1

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

height = tree.get_height(tree.root)
print(height)
