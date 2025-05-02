from collections import defaultdict, deque

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)  # Adjacency list
        self.in_degree = defaultdict(int)  # Track incoming edges

    # Add edge from u to v
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1
        if u not in self.in_degree:
            self.in_degree[u] = 0

    # Topological Sort using Kahn's Algorithm (BFS)
    def topological_sort(self):
        queue = deque()
        result = []

        # Start with all nodes having in-degree 0
        for node in self.in_degree:
            if self.in_degree[node] == 0:
                queue.append(node)

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.graph[current]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(self.in_degree):
            return "❌ Graph has a cycle; topological sort not possible"
        
        return result

# Example usage
if __name__ == "__main__":
    dg = DirectedGraph()
    dg.add_edge("A", "C")
    dg.add_edge("B", "C")
    dg.add_edge("B", "D")
    dg.add_edge("C", "E")
    dg.add_edge("D", "F")
    dg.add_edge("E", "F")

    print("Topological Sort:", dg.topological_sort())