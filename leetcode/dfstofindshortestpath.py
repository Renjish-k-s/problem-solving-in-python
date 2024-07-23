import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []  # Initialize adjacency list for destination node
        self.graph[u].append((v, weight))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(str(neighbor) for neighbor, _ in self.graph[node]))

    def shortest_path(self, start, end):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]  # Priority queue
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > distances[curr_node]:
                continue
            for neighbor, weight in self.graph[curr_node]:
                distance = curr_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances[end]

# Example usage:
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 2)

print("Shortest distance from 0 to 3:", g.shortest_path(0, 3))
