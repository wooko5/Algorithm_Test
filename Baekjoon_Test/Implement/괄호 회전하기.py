def solution(s):
    answer = 0
    
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        stack = []
        for tmp in temp:
            if not stack:
                stack.append(tmp)
            else:
                if stack[-1] == '(' and tmp == ')':
                    stack.pop()
                elif stack[-1] == '[' and tmp == ']':
                    stack.pop()
                elif stack[-1] == '{' and tmp == '}':
                    stack.pop()
                else:
                    stack.append(tmp)
        if not stack:
            answer += 1
    return answer

s = "[](){}"
print(solution(s))