num_people = int(input())
time_withdraw = list(map(int, input().split()))

for i in range(1, len(time_withdraw)):
    for j in range(i, 0, -1):
        if time_withdraw[j] < time_withdraw[j-1]:
            time_withdraw[j], time_withdraw[j-1] = time_withdraw[j-1], time_withdraw[j]
        else:
            break

total = 0
result = []
for i in time_withdraw:
    total += i
    result.append(total)

print(sum(result))