def solution(arr):
    answer = [-1]
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
    answer.pop(0)
    return answer

print(solution([1,1,1,3,3,5]))