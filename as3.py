class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V

        # Use a priority queue to store vertices with their current distances
        pq = [(0, src)]

        while pq:
            current_dist, current_vertex = pq.pop(0)

            if visited[current_vertex]:
                continue

            visited[current_vertex] = True

            for neighbor, weight in self.graph[current_vertex]:
                if not visited[neighbor] and dist[current_vertex] + weight < dist[neighbor]:
                    dist[neighbor] = dist[current_vertex] + weight
                    pq.append((dist[neighbor], neighbor))
                    pq.sort()

        return dist

# User input for graph
num_vertices = int(input("Enter the number of vertices in the graph: "))
g = Graph(num_vertices)

num_edges = int(input("Enter the number of edges in the graph: "))
for _ in range(num_edges):
    u, v, weight = map(int, input("Enter edge (u, v) and its weight: ").split())
    g.add_edge(u, v, weight)

# User input for source vertex
source_vertex = int(input("Enter the source vertex: "))

# Run Dijkstra's algorithm
distances = g.dijkstra(source_vertex)

# Print the shortest distances
print("Shortest distances from the source vertex:")
for i, distance in enumerate(distances):
    print(f"Vertex {i}: {distance}")
