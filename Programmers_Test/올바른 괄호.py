"""
처음에는 공식이 있을 것 같아서 앞뒤 '(, )' and 두 괄호의 숫자가 같으면 True를 반환했는데
테스트케이스 5, 11만 맞지를 않았다(효율성이나 정확성 나머지는 전부 맞춤)
인터넷으로 힌트를 찾더니 stack으로 풀면 된다고 해서 혼자 잘 풂
문자열 문제는 스택쓰기 좋은 것 같다
2021.07.08 
"""

def solution(s):
    stack = []
    for bracket in s:
        if not stack:
            stack.append(bracket)
        else:
            if stack[-1] == '(' and bracket == ')':
                stack.pop()
            else:
                stack.append(bracket)

    if not stack:
        return True
    return False



s = "())(()"
print(solution(s))