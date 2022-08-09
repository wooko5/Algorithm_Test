"""
기능개발 문제였다!!
그 전 과는 다른 방식의 풀이
2021.07.12
"""

def solution(progresses, speeds):
    answer = []
    array = []

    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] != 0:
            array.append((100-progresses[i]) // speeds[i]+1)
        else:
            array.append((100-progresses[i]) // speeds[i])

    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i+1] = array[i]
    
    for i in range(1, 101):
        cnt = 0 
        for j in array:
            if i == j:
                cnt += 1
        if cnt != 0:
            answer.append(cnt)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))