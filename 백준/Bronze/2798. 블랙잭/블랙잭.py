import sys

N, M = list(map(int, sys.stdin.readline().split()))
card_numbers = list(map(int, sys.stdin.readline().split()))

total = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card_numbers[i] + card_numbers[j] + card_numbers[k] > M:
                continue
            else:
                total = max(total, card_numbers[i] + card_numbers[j] + card_numbers[k])

print(total)
