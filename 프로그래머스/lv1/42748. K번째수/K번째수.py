def solution(array, commands):
    answer = [sorted(array[command[0]-1:command[1]])[command[2]-1] for command in commands]
    return answer