class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_odd_level_nodes(root):
    if root is None:
        return
    
    queue = [root]
    level = 0
    
    while queue:
        level += 1
        size = len(queue)
        
        for i in range(size):
            node = queue.pop(0)
            
            if level % 2 != 0:
                print(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# create a binary tree
root = Node(5)
root.left = Node(2)
root.right = Node(-3)
root.left.left = Node(4)
root.left.right = Node(3)
root.right.left = Node(1)
root.right.right = Node(-2)

print("Nodes at odd levels:")
print_odd_level_nodes(root)
