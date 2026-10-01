import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3)],
    'C': [('D', 2)],
    'D': [('G', 4)],
    'G': []
}

h = {'A': 6, 'B': 5, 'C': 6, 'D': 4, 'G': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        if node in visited:
            continue
        visited.add(node)
        for next_node, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[next_node]
            heapq.heappush(
                pq, (new_f, new_g, next_node, path + [next_node])
            )

path, cost = astar('A', 'G')
print("Shortest Path:", "->".join(path))
print("Total Distance:", cost)
