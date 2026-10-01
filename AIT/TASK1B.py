def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=" ")

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input())
e = int(input())

graph = [[] for i in range(n)]

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input())

visited = [False] * n

dfs(graph, start, visited)
