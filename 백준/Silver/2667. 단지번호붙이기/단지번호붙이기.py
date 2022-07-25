village = int(input())

graph = []
for i in range(village):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= village or y <= -1 or y >= village:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


cnt = 0
result = 0
num_village = []
for i in range(village):
    for j in range(village):
        if dfs(i, j):
            result += 1
            num_village.append(cnt)
            cnt = 0

print(result)
for i in sorted(num_village):
    print(i)