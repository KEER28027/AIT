def is_safe(graph, color, v, c, n):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def solve(graph, color, v, n, m):
    if v == n:
        return True
    for c in range(1, m + 1):
        if is_safe(graph, color, v, c, n):
            color[v] = c
            if solve(graph, color, v + 1, n, m):
                return True
            color[v] = 0
    return False

n = int(input("Enter no. of vertices:"))
m = int(input("Enter no. of colors:"))
print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

color = [0] * n

if solve(graph, color, 0, n, m):
    print("Valid coloring exists")
    print("Colors:", *color)
else:
    print("No valid coloring exists")
