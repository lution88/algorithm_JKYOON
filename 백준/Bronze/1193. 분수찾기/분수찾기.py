cnt = int(input())

num = 0
total_num = 0

# cnt = 55
while total_num < cnt: # total이라는건 이전 수들의 갯수 
    num += 1          # 몇 번째 줄 1 2 3  4  5  6  7  8  9  10
    total_num += num # 총 줄의 개수 1 3 6 10 15 21 28 36 45  55

# total_num -= num # 줄의 수  15 - 5 = 10 total_num = 이전 수들의 갯수 10개
before_total_num = total_num - num
now_num = total_num - before_total_num

if now_num % 2 != 0: # 홀수 : 분자가 큰 순서로 시작
    x = cnt - before_total_num # 11 - 10 = 1
    y = num - x + 1 # 5 - 1 + 1 = 5
else: #  짝수 : 분모가 큰 순서로 시작
    y = cnt - before_total_num # 12 - 10 = 2 
    x = num - y + 1  # 5 - 2 + 1 = 4

print(f'{y}/{x}')