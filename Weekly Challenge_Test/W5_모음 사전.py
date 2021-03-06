"""
어떤 문자가 첫 번째 문자로 나올 경우의 수는 (5^1 + 5^2 + 5^3 + 5^4 + 5^5) / 5 = 781이다
어떤 문자가 두 번째 문자로 나올 경우의 수는 (5^1 + 5^2 + 5^3 + 5^4) / 5 = 156이다
어떤 문자가 세 번째 문자로 나올 경우의 수는 (5^1 + 5^2 + 5^3) / 5 = 31이다
어떤 문자가 네 번째 문자로 나올 경우의 수는 (5^1 + 5^2) / 5 = 6이다
어떤 문자가 다섯 번째 문자로 나올 경우의 수는 (5^1) / 5 = 1이다
예를 들어 'AIU'의 순서는 (781 * A의 인덱스 + 1) + (156 * I의 인덱스 + 1) + (31 * U의 인덱스 + 1) 
= (781*0 + 1) + (156*2 + 1) + (31*4 + 1) = 1  + 313 + 125 = 439
어떻게 보면 간단한 순열문제로 풀 수 있었지만 초기에 문제 접근을 난잡하게 하는 바람에 해답을 찾기 힘들었다
2021.09.06
"""

def solution(word):
    answer = 0
    case = [781, 156, 31, 6, 1]
    string = "AEIOU"
    for i in range(len(word)):
        answer += string.index(word[i]) * case[i] + 1
    return answer
word = "AAAAE"
print(solution(word))