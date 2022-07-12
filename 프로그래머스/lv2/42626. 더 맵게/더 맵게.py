import heapq


def solution(scoville, K):
    heapq.heapify(scoville) # heapq 선언
    answer = 0
    scoville_index = 1

    while scoville_index <= len(scoville)-1:
        min1 = heapq.heappop(scoville) # 가장 작은 원소를 pop
        if min1 >= K:
            return answer
        else:
            min2 = heapq.heappop(scoville) # 두 번째 작은 원소를 pop
            heapq.heappush(scoville, min1 + (min2 * 2)) # 스코빌 지수 섞어서 push
            answer += 1

    if scoville[0] > K:
        return answer
    else:
        return -1
