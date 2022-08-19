import sys

n = int(sys.stdin.readline())

join_list = [sys.stdin.readline().split() for _ in range(n)]
join_list.sort(key=lambda x : int(x[0]))

for member in join_list:
    print(member[0], member[1])