"""
처음에는 그리디같았는데 생각해보니 
(가장 작은 수 * 가장 큰 수)로 한다면 모두 중간값에 가깝게 나와서
최소값이 나오지 않을까 생각했고, 그래서 A는 오름차순, B는 내림차순으로 정렬하고
두 배열의 길이가 같으므로 서로 곱해서 누적합(answer)를 계산했다
2021.07.05
"""

def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for i in range(len(A)):
        temp = A[i] * B[i]
        answer += temp
    return answer

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))
