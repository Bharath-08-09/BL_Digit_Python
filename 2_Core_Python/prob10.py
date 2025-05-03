from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # Move key to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove least recently used item (first one)
            self.cache.popitem(last=False)

    def display(self):
        print("Current Cache:", list(self.cache.items()))


# 🔍 Example usage
if __name__ == "__main__":
    lru = LRUCache(3)
    
    lru.put(1, 'A')
    lru.put(2, 'B')
    lru.put(3, 'C')
    lru.display()  # Output: [(1, 'A'), (2, 'B'), (3, 'C')]

    print("Accessing key 2:", lru.get(2))  # Output: 'B'
    lru.display()  # Output: [(1, 'A'), (3, 'C'), (2, 'B')]

    lru.put(4, 'D')  # Evicts key 1
    lru.display()  # Output: [(3, 'C'), (2, 'B'), (4, 'D')]

    print("Accessing key 1:", lru.get(1))  # Output: -1 (not found)