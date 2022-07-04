"""
1 번째: 35.1 / 100.0, 정확성: 19.8, 효율성: 15.3
2 번째: 38.4 / 100.0, 정확성: 23.1, 효율성: 15.3 (answer가 0인 경우 1을 리턴하게 추가함)
3 번째: 58.3 / 100.0, 정확성: 42.9, 효율성: 15.3 (break을 넣어서 연속적이지 않다면 나오기)
4 번째: 61.6 / 100.0, 정확성: 46.2, 효율성: 15.3 (문자열의 크기가 1인 경우)
5 번째: 71.5 / 100.0, 정확성: 56.1, 효율성: 15.3 (i의 범위를 전체로 확장)
6 번째: 100.0 / 100.0, 정확성: 69.3, 효율성: 30.7 (인터넷에서 팰린드롬을 나눠서 하는 힌트를 보고 맞춤)
"""

def isPalindrome(array):
    if array == array[::-1]:
        return True
    return False

def solution(s):
    answer = 0
    for i in range(len(s)): # s의 최대 길이가 7이면, i는 0~6, j는 1 ~ 7이다
        for j in range(i+1, len(s)+1):
            if isPalindrome(s[i:j]):
                if answer < len(s[i:j]):
                    answer = len(s[i:j])
    return answer

s = "abcdcba"
print(solution(s))

"""
def solution(s): # 초기 형태의 코드
    answer = 0
    for i in range(1, len(s)//2+1):
        count = 1 

        for j in range(1, i+1):
            if i-j >= 0 and i+j < len(s):
                if s[i+j] == s[i-j]:
                    count += 2
        if answer < count:
            answer = count
    if answer == 0:
        return 1
    return answer
"""