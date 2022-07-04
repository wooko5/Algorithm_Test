"""
3일 동안 코테를 안 풀다가 첨으로 푼 문제(level 1이라 2분만에 풂) 
역시나 막상 코테풀면 재미있게 하면서 하하하 
앞으로도 ㅍㅇㅌ!!!
2021.07.19
"""

def solution(n):
    answer = ''
    n = list(str(n))
    n.sort(reverse = True)
    for i in n:
        answer += i
    return int(answer)

n = '1189383'
print(solution(n))