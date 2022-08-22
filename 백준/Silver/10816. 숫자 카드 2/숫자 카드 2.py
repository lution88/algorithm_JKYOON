N = int(input())
nums_of_N = list(map(int, input().split()))

M = int(input())
checks_of_M = list(map(int, input().split()))

key_hash = {}
for key in nums_of_N:
    if key in key_hash:
        key_hash[key] += 1
    else:
        key_hash[key] = 1

for key in checks_of_M:
    if key in key_hash:
        print(key_hash[key], end=' ')
    else:
        print(0, end=' ')