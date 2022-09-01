def solution(numbers):
    nums = [i for i in range(10) if i not in numbers]
    return sum(nums)