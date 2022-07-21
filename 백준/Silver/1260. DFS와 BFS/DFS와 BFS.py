import sys
from collections import deque

def dfs(graph, n, visited):
    # 현재 노드 방문 처리
    visited[n] = 1
    print(n, end=' ')
    # 방문하지 않은 인접 노드
    for i in graph[n]:
        if visited[i] == 0:
            dfs(graph, i, visited)

def bfs(graph, s, visited):
    # 큐 구현
    queue = deque([s])    
    # 현재 노드를 방문처리
    visited[s] = 1
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 원소를 하나씩 뽑아 출력.
        a = queue.popleft()
        print(a, end=' ')
        # 아직 방문하지 않은 인접한 원소를 큐에 넣는다.
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

# 노드의 개수(정점의개수) = n
# 간선의 개수 = m  간선은 양방향
# 탐색을 시작할 노드의 번호 = v

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()
    
visited = [0] * (n+1)
dfs(graph, v, visited)
print()
visited = [0] * (n+1)
bfs(graph, v, visited)