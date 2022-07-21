import sys

total_computer = int(sys.stdin.readline())
com_nets = int(sys.stdin.readline())

graph_nets = [[] for _ in range(total_computer + 1)]

for _ in range(com_nets):
    x, y = map(int, sys.stdin.readline().split())
    graph_nets[x].append(y)
    graph_nets[y].append(x)


virus_com = [0] * (total_computer+1)

def dfs(graph_nets, n, virus_com):
    virus_com[n] = 1
    
    for i in graph_nets[n]:
        if not virus_com[i] == 1:
            dfs(graph_nets, i, virus_com)
    return True

dfs(graph_nets, 1, virus_com)
print(sum(virus_com)-1)