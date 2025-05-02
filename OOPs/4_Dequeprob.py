class Deque:
    def __init__(self):
        self.items = []

    # Add an element to the front of the deque
    def add_front(self, item):
        self.items.insert(0, item)

    # Add an element to the rear of the deque
    def add_rear(self, item):
        self.items.append(item)

    # Remove an element from the front of the deque
    def remove_front(self):
        if self.is_empty():
            return "❌ Deque is empty"
        return self.items.pop(0)

    # Remove an element from the rear of the deque
    def remove_rear(self):
        if self.is_empty():
            return "❌ Deque is empty"
        return self.items.pop()

    # Check if the deque is empty
    def is_empty(self):
        return len(self.items) == 0

    # (Optional) Display the current deque contents
    def display(self):
        return self.items

# Example usage
if __name__ == "__main__":
    dq = Deque()

    dq.add_rear(10)
    dq.add_rear(20)
    dq.add_front(5)
    dq.add_front(1)

    print("Deque Contents:", dq.display())

    print("Remove from front:", dq.remove_front())
    print("Remove from rear:", dq.remove_rear())

    print("Is Deque Empty?", dq.is_empty())
    print("Final Contents:", dq.display())