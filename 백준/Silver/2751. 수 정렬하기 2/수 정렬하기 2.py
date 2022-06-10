import sys

num = int(sys.stdin.readline())
new_num = [int(sys.stdin.readline()) for _ in range(num)]

new_num.sort()
for i in new_num:
    print(i)