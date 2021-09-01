def solution(a,b):
    answer = 0
    for i in range(len(a)):
        temp = a[i]*b[i]
        answer += temp
    return answer