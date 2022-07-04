"""
처음에는 while문과 for문을 이용한 이중 반복문으로 풀었지만 생각해보니 s의 길이가 100만이라 너무 커서 시간초과
이후에 stack을 이용한 코드를 참조해서 정리 및 해결, 다음에도 함 다시 풀어보면 좋을듯
stack을 통한 간단한 원리와 구현
2021.07.01
"""
def solution(s):
    stack = []
    for char in s:
        if stack: # stack이 비어있지 않다면
            if stack[-1] == char: # stack의 마지막 문자가 지금 나온 문자와 같다면 
                stack.pop() # stack의 마지막 원소 비우기
            else:
                stack.append(char) # stack의 마지막 문자가 지금 나온 문자와 다르다면, 문자 삽입
        else: # stack이 비어있으면 문자넣기
            stack.append(char)

    return 0 if stack else 1 # pythonic한 코드
s = "cdcd"
s = "baabaa"
print(solution(s))