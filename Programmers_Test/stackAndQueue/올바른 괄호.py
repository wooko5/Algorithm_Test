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