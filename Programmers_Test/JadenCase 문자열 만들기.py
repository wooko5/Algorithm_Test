"""
문자열로 풀지 배열로 바꿔서 풀지 생각하다가 
문자열은 assignment가 힘들어서 예를 들면, a[1] = 2
배열로 바꿨다가 한번에 문자열로 반환하는 방식으로 풀었다
isdigit()말고 isnumemric을 써도 된다.
쉬운 문제
2021.07.06
"""

def solution(s):
    s = list(s)
    if not s[0].isdigit() and s[0].islower():
        s[0] = s[0].upper()
        
    for i in range(1, len(s)):
        if s[i-1] == ' ': # 바로 뒷문자가 공백이라면 다음 문자는 무조건 대문자
            if not s[i].isdigit() and s[i].islower():
                s[i] = s[i].upper()
        else:
            if s[i].isupper():
                s[i] = s[i].lower()
    return ''.join(s)
s = "3people unFollowed me"
print(solution(s))