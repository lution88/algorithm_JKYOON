def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]
    
    win_cnt = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
        elif lotto in win_nums:
            win_cnt += 1
    
    min_result = win_cnt
    max_result = win_cnt + zero_cnt
    
    return [answer[max_result], answer[min_result]]
