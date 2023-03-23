class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if root is None:
        return 0
    
    queue = [root]
    max_sum = root.val
    max_level = 0
    level = 0
    
    while queue:
        level += 1
        level_sum = 0
        size = len(queue)
        
        for i in range(size):
            node = queue.pop(0)
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
            
    return max_level

# create a binary tree
root = Node(5)
root.left = Node(2)
root.right = Node(-3)
root.left.left = Node(4)
root.left.right = Node(3)
root.right.left = Node(1)
root.right.right = Node(-2)

print("Maximum level sum:", max_level_sum(root))
