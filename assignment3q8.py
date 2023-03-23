class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_sum_x(root, x):
    if root is None:
        return 0
    
    count = 0
    if root.val == x:
        count += 1
    
    count += count_subtrees_with_sum_x(root.left, x)
    count += count_subtrees_with_sum_x(root.right, x)
    
    subtree_sum = root.val
    subtree_sum += sum_subtree(root.left)
    subtree_sum += sum_subtree(root.right)
    
    if subtree_sum == x:
        count += 1
    
    return count

def sum_subtree(root):
    if root is None:
        return 0
    else:
        return (root.val + sum_subtree(root.left) + sum_subtree(root.right))

# create a binary tree
root = Node(5)
root.left = Node(2)
root.right = Node(-3)
root.left.left = Node(4)
root.left.right = Node(3)
root.right.left = Node(1)
root.right.right = Node(-2)

x = 6
print("Number of subtrees with sum", x, ":", count_subtrees_with_sum_x(root, x))
