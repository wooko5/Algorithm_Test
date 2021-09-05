"""
쉽게 잘 풀었다 대략 15분도 안 걸린듯, 효율성과 정확성도 높지만 코드가 너무 길다
파이써닉한 코드를 원한다면 라이브러리 함수 사용에 좀더 유의해야겠다
def solution(n):
    c = bin(n).count('1') # bin(n)은 숫자를 문자열의 이진수로 변환하는 함수, 이를 통해 1의 개수를 알아내고 
    for number in range(n+1,1000001): # n+1부터 1000001까지의 숫자를 차례대로 순회하면서 
        if bin(number).count('1') == c: # 만약에 c와 같은 개수의 숫자가 존재한다면
            return number # number를 반환
"""

def binary(number):
    if number == 0:
        return '0'
    
    result = ''
    while number > 1:
        temp = number // 2
        if number % 2 == 1:
            result += '1'
        else:
            result += '0'
        number = temp
    
    result += '1'
    return result[::-1]

def count(s):
    cnt = 0
    for i in s:
        if i == '1':
            cnt += 1
    return cnt

def solution(n):
    binary_n = binary(n)
    n_cnt = count(binary_n)
    answer = n + 1

    while True:
        if count(binary(answer)) == n_cnt:
            break
        answer += 1
    return answer

n = 15
print(solution(n))