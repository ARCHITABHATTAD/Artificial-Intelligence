import heapq
import numpy as np

maze = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
])

# Print maze
for row in maze:
    for cell in row:
        print('X' if cell == 1 else '_', end=' ')
    print()

# Take user input for start and goal positions
start = tuple(map(int, input("Enter the start position (row column): ").split()))
goal = tuple(map(int, input("Enter the goal position (row column): ").split()))

# Define the possible movements (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(position):
    # Manhattan distance heuristic
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def a_star(maze, start, goal):
    open_list = []
    closed_set = set()
    costs = {start: 0}
    parents = {start: None}
    heapq.heappush(open_list, (heuristic(start), start))

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            # Goal reached, reconstruct the path
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        closed_set.add(current)

        for move in moves:
            next_pos = (current[0] + move[0], current[1] + move[1])

            if (
                0 <= next_pos[0] < maze.shape[0]
                and 0 <= next_pos[1] < maze.shape[1]
                and maze[next_pos] == 0
                and next_pos not in closed_set
            ):
                new_cost = costs[current] + 1

                if (
                    next_pos not in costs
                    or new_cost < costs[next_pos]
                ):
                    costs[next_pos] = new_cost
                    parents[next_pos] = current
                    heapq.heappush(open_list, (new_cost + heuristic(next_pos), next_pos))

    return []

# Run the A* algorithm
path = a_star(maze, start, goal)

print("-------------- SOLUTION --------------------")

# Display the maze and path
for i, row in enumerate(maze):
    for j, cell in enumerate(row):
        if (i, j) == start:
            print('S', end=' ')
        elif (i, j) == goal:
            print('G', end=' ')
        elif (i, j) in path:
            print('*', end=' ')
        elif cell == 1:
            print('X', end=' ')
        else:
            print('_', end=' ')
    print()
    
print(path)
