import heapq
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    g_cost = {start: 0}
    parent = {start: None}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        f, current = heapq.heappop(pq)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for dr, dc in directions:
            nr = current[0] + dr
            nc = current[1] + dc

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == 1:
                    continue

                neighbor = (nr, nc)
                new_g = g_cost[current] + 1

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + heuristic(neighbor, goal)

                    heapq.heappush(pq, (f, neighbor))
                    parent[neighbor] = current
    return None
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
path = a_star(grid, start, goal)
print("Grid:")
for row in grid:
    print(row)
print("\nShortest Path:")
print(path)
print("\nPath Length:", len(path) - 1)
