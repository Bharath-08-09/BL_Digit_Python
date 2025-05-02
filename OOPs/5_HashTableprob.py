class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    # Hash function: simple modulo
    def _hash(self, key):
        return hash(key) % self.size

    # Insert a key-value pair
    def insert(self, key, value):
        index = self._hash(key)

        original_index = index
        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("❌ Hash table is full")

        self.keys[index] = key
        self.values[index] = value
        print(f"✅ Inserted key '{key}' at index {index}")

    # Retrieve a value by key
    def get(self, key):
        index = self._hash(key)
        original_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    # Check if a key exists
    def contains(self, key):
        return self.get(key) is not None

    # Display table contents (for debugging)
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.keys[i]} → {self.values[i]}")

# Example usage
if __name__ == "__main__":
    ht = HashTable()

    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("grape", 150)

    print("\n🍎 Value for 'apple':", ht.get("apple"))
    print("🍌 Value for 'banana':", ht.get("banana"))
    print("🍇 Does 'grape' exist?", ht.contains("grape"))
    print("🍓 Does 'strawberry' exist?", ht.contains("strawberry"))

    print("\n📘 Hash Table State:")
    ht.display()