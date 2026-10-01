from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    q = deque([start])
    visited[start] = True
    level = 0

    while q and level <= 3:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            print(node, end=" ")

            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        level += 1

n = int(input())
e = int(input())

graph = [[] for _ in range(n)]

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input())

bfs(graph, start)
