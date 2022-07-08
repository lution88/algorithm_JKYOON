import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

key_hash = {}
for key in a:
    key_hash[key] = True

for key in b:
    if key_hash.get(key):
        print(1)
    else:
        print(0)