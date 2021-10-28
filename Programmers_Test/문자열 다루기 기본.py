def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False

s = 'a134'
s = '1234'
print(solution(s))