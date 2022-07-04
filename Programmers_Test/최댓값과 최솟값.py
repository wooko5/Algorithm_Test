"""
레벨 2 답지 않은 문제였다 매우 쉬움 
2021.07.06
"""

def solution(s):
    array = list(map(int, s.split()))
    return str(min(array)) + ' ' + str(max(array))

s = "1 2 3 4"
s = "-1 -2 -3 -4"
print(solution(s))