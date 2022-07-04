"""
연속성에 집중해서 LCS(가장 긴 증가수열)을 이용해서 풀었다
쉬운 문제였다 
2021.07.06
"""

def solution(n):
    cnt = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            if temp == n:
                cnt += 1
                break
            elif temp > n:
                break
            temp += j
    return cnt+1

n = 15
print(solution(n))