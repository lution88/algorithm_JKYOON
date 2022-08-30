def solution(board, moves):
    
    stacks = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stacks.append(board[i][move-1])
                board[i][move-1] = 0
                break
        
    temp = []
    cnt = 0
    for stack in stacks:
        if len(temp) == 0:
            temp.append(stack)
            continue
        
        if temp[-1] == stack:
            temp.pop()
            cnt += 2
        else:
            temp.append(stack)
        
    return cnt