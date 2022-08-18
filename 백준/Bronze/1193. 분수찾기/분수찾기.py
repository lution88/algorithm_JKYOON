cnt = int(input())

num = 0
total_num = 0

while total_num < cnt:
    num += 1
    total_num += num

before_total_num = total_num - num
now_num = total_num - before_total_num

if now_num % 2 != 0:
    x = cnt - before_total_num
    y = num - x + 1
else:
    y = cnt - before_total_num
    x = num - y + 1

print(f'{y}/{x}')