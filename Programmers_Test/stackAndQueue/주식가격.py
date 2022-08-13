"""
def solution(prices): # 처음에 생각했던 코드
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

나중에 다시 풀때 또 비슷하게 함...
def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        index = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
            elif j == len(prices) - 1:
                answer.append(j - i)
                
    answer.append(0)
    return answer

stack을 이용한 방법이 2배 더 빠른 것을 알게 됐다
이후에 여러가지 방법을 해봤지만 정확도에서 떨어졌고 
참고를 통해 코드완성 휴우,,, 
다시한번 봐야겠다 
2021.07.15
"""

def solution(prices):
    answer = [0]*len(prices)
    stack = [] # 인덱스를 저장(인덱스가 곧 시간)
    
    for i, price in enumerate(prices): # 인덱스, 원소값 나옴
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)    
    
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))