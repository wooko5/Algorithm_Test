"""
처음에 생각한 'S를 일정하게 나누는게 가장 큰 곱셈 결과'를 생각해냈고
첫번째 사이트에서 힌트를 얻어서 구현에 성공했다
컨셉만 알고있다면 굉장히 쉬운문제! 컨셉을 더 구체화하기 위한 집중력이 필요하다
2021.07.21
"""

def solution(n, s):
    if n > s:
        return [-1]

    answer = []
    temp = s // n

    for _ in range(n):
        answer.append(temp)
    
    for i in range(len(answer)-1, len(answer)-1-(s%n), -1):
        answer[i] += 1
    
    return answer


n = 3
s = 8
print(solution(n,s))