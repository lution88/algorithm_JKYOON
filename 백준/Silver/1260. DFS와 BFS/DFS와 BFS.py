import sys
from collections import deque


def dfs(graph, n, visited):
    visited[n] = 1
    print(n, end=' ')
    for i in graph[n]:
        if visited[i] == 0:
            dfs(graph, i, visited)


def bfs(graph, s, visited):
    queue = deque([s])
    visited[s] = 1

    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()

visited = [0] * (n + 1)
dfs(graph, v, visited)
print()
visited = [0] * (n + 1)
bfs(graph, v, visited)