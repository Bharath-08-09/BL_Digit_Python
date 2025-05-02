import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []

    # Insert element with a given priority
    def insert(self, item, priority):
        heapq.heappush(self._heap, (priority, item))
        print(f"✅ Inserted '{item}' with priority {priority}")

    # Delete and return the element with the highest priority (lowest number)
    def delete_highest_priority(self):
        if self.is_empty():
            return "❌ Priority Queue is empty"
        priority, item = heapq.heappop(self._heap)
        print(f"🗑️ Removed '{item}' with priority {priority}")
        return item

    # Check if the priority queue is empty
    def is_empty(self):
        return len(self._heap) == 0

    # Optional: Display current state of the queue
    def display(self):
        print("📋 Current Queue:")
        for priority, item in sorted(self._heap):
            print(f" - {item} (priority: {priority})")

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.insert("Task A", 3)
    pq.insert("Task B", 1)
    pq.insert("Task C", 2)

    pq.display()

    pq.delete_highest_priority()
    print("Is queue empty?", pq.is_empty())

    pq.display()