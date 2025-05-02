class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    # Base case: empty tree is a BST
    if node is None:
        return True
    
    # Check BST property
    if not (min_val < node.value < max_val):
        return False

    # Check recursively for left and right subtrees
    return (is_bst(node.left, min_val, node.value) and
            is_bst(node.right, node.value, max_val))

# Example usage
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("Is BST:", is_bst(root))  # ✅ Should return True