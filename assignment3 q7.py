class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_nodes(root):
    if root is None:
        return 0
    else:
        return (root.val + sum_nodes(root.left) + sum_nodes(root.right))

# create a perfect binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Sum of all nodes:", sum_nodes(root))
