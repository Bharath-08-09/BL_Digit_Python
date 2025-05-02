class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new value into the tree
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if current is None:
            return Node(value)
        if value < current.value:
            current.left = self._insert_recursive(current.left, value)
        elif value > current.value:
            current.right = self._insert_recursive(current.right, value)
        return current

    # Search for a value in the tree
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    # In-order traversal (Left, Root, Right)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    print("🔁 In-order Traversal:", bst.inorder_traversal())
    print("🔍 Search 60:", bst.search(60))
    print("🔍 Search 25:", bst.search(25))