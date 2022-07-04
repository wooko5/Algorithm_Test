"""
파이썬 라이브러리 함수인 bin()함수를 이용하는 것도 좋지만 format()함수를 이용해서 해봤다
간단하게 구현을 통해 쉽게 풀었다

def solution(s): # bin()함수 이용
    cnt_total = 0
    cnt_zero = 0
    
    while s != '1':
        temp = ''
        cnt_total += 1
        for string in s:
            if string == '0':
                cnt_zero += 1
            else:
                temp += string
        length = len(temp)
        s = bin(length)[2:] # 앞의 2글자를 제외하면 우리가 아는 이진수이므로
    return [cnt_total, cnt_zero]


2021.07.16
"""

def solution(s):
    cnt_total = 0
    cnt_zero = 0
    
    while s != '1':
        temp = ''
        cnt_total += 1
        for string in s:
            if string == '0':
                cnt_zero += 1
            else:
                temp += string
        length = len(temp)
        s = format(length, 'b')
    return [cnt_total, cnt_zero]

s = "110010101001"
print(solution(s))