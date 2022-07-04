"""
LCM(최소공배수)과 GCD(최대공약수)는 라이브러리 함수가 존재한다
하지만 직접 구현해보았다, 두 개 숫자의 최소공배수를 구하는 방법을 알고있다면
N개의 최소공배수를 구하는 것은 배열에 있는 원소를 다 하나씩 비교해가면 된다
쉬운 문제
2021.07.06 
"""

def LCM(A, B):
    for number in range(max(A,B), A*B+1):
        if number % A == 0 and number % B == 0:
            return number

def solution(arr):
    arr.sort()
    result = [LCM(arr[0], arr[1])]
    for i in range(2, len(arr)):
        temp = LCM(result[-1], arr[i])
        result.append(temp)
    return result[-1]

arr = [2, 6, 8, 14]
print(solution(arr))