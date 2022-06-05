n = int(input())

def solution(n):
    cnt = []
    def hanoi(n, start, end):
        if n == 0:
            return

        middle = 6 - start - end

        hanoi(n-1, start, middle)
        # print(f"{start} {end}")
        cnt.append([start, end])
        hanoi(n-1, middle, end)

    hanoi(n, 1, 3)
    print(len(cnt))
    for i, j in cnt:
        print(i, j)

solution(n)