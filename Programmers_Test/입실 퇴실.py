def count(stack, temp, answer):
    for i in stack:
        if answer[i-1] < temp:
            answer[i-1] += temp
    return answer
    
def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    stack = [enter.pop(0)]
    
    while leave:
        if leave[0] not in stack and enter:
            stack.append(enter.pop(0))
        elif leave[0] in stack:
            if len(stack) >= 2:
                temp = len(stack) - 1
                answer = count(stack, temp, answer)
            stack.remove(leave.pop(0))
    return answer

enter = [1, 4, 2, 3]
leave = [2, 1, 3, 4]
print(solution(enter, leave))