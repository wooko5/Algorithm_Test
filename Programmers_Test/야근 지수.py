"""
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    while n > 0:
        works[works.index(max(works))] -= 1
        n -= 1
    for number in works:
        answer += number**2
    return answer
이제는 먹히지않는 코드
2021.07.08
"""

import heapq
def solution(n, works):
    answer = 0
    array = []

    if sum(works) <= n:
        return 0
    
    for number in works:
        heapq.heappush(array, (-number, number)) # 최대힙을 만들기 위한 (우선순위, 숫자)
    
    while n > 0:
        temp = heapq.heappop(array)[1] # 최대값을 뽑기
        temp -= 1
        heapq.heappush(array, (-temp, temp))
        n -= 1
        
    for i in array:
        answer += i[1]**2
    return answer

works = [1, 1, 1]
n = 4
print(solution(n, works))