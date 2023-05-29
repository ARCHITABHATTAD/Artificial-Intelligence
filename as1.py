from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, v):
        visited = set()
        queue = []

        visited.add(v)
        queue.append(v)

        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs_search(self, v, target, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(v)
        path.append(v)

        if v == target:
            return True, path

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                found, result_path = self.dfs_search(neighbor, target, visited, path)
                if found:
                    return True, result_path

        path.pop()
        return False, []

    def bfs_search(self, v, target):
        visited = set()
        queue = []

        visited.add(v)
        queue.append([v, [v]])  # Each element in the queue is [vertex, path]

        while queue:
            current, path = queue.pop(0)

            if current == target:
                return True, path

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor, path + [neighbor]])

        return False, []

# Create a graph
g = Graph()

# Take user input for number of edges
num_edges = int(input("Enter the number of edges: "))

# Take user input for edges
for _ in range(num_edges):
    u, v = map(int, input("Enter an edge (u v): ").split())
    g.add_edge(u, v)

# Take user input for starting vertex
start_vertex = int(input("Enter the starting vertex: "))

# Take user input for the target vertex to search
target_vertex = int(input("Enter the target vertex to search: "))

# Perform DFS starting from the given vertex
print("DFS Traversal:")
visited = set()
g.dfs(start_vertex, visited)
print()

# Perform BFS starting from the given vertex
print("BFS Traversal:")
g.bfs(start_vertex)
print()

# Search for the target vertex using DFS
found_dfs, path_dfs = g.dfs_search(start_vertex, target_vertex)
if found_dfs:
    print("Target vertex found using DFS")
    print("Path:", path_dfs)
else:
    print("Target vertex not found using DFS")

# Search for the target vertex using BFS
found_bfs, path_bfs = g.bfs_search(start_vertex, target_vertex)
if found_bfs:
    print("Target vertex found using BFS")
    print("Path:", path_bfs)
else:
    print("Target vertex not found using BFS")
