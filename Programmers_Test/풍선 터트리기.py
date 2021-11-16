"""
처음에 어떻게 접근할지 몰라서 인터넷을 보다가 생각해보니
조건1: 기준값의 오른쪽에 있는 숫자들 중에 기준값보다 작은 값이 있다.
조건2: 기준값의 왼쪽에 있는 숫자들 중에 기준값보다 작은 값이 있다. 
조건1과 조건2를 동시에 만족하면(and) 절대 기준값을 남길 수 없다.
이를 이용해서 해당 기준값을 끝까지 남길 수 없을지 있을지 확인하면 된다
2021.11.16 프로그래머스 레벨 3, 월간 코드 챌린지 1
"""

def solution(a):
    answer = 2
    start, end = a[0], a[-1]
    
    if len(a) <= 2:
        return answer
    
    for i in range(1, len(a) - 1):
        if start > a[i]:
            answer += 1
            start = a[i]
            
        if end > a[-1-i]:
            answer += 1
            end = a[-1-i]
            
    return answer if start != end else answer - 1