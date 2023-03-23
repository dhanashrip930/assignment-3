class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_left_leaves(root):
    if root is None:
        return 0
    
    result = 0
    stack = [(root, False)]
    
    while stack:
        node, is_left = stack.pop()
        
        if node.left is None and node.right is None and is_left:
            result += node.val
        
        if node.left:
            stack.append((node.left, True))
        
        if node.right:
            stack.append((node.right, False))
            
    return result

# example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(sum_left_leaves(root))
