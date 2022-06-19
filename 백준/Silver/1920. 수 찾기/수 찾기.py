num_n = int(input())
group_a = sorted(map(int, input().split()))

num_m = int(input())
group_b = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return None
    # 중간점 설정
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 변환
    if arr[mid] == target:
        return mid
    # 찾는 값이 중간점보다 작은경우
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    # 찾는 값이 중간점보다 큰 경우
    else:
        return binary_search(arr, target, mid+1, end)


for i in group_b:
    start, end = 0, num_n-1
    result = binary_search(group_a, i, start, end)
    if result == None:
        print(0)
    else:
        print(1)
