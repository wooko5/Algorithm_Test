# 다시 한번 도전해보기
n = int(input())
math_expression = list(input())
answer = int(math_expression[0])
# 0, 2, 4, ... 등의 index에는 숫자만 들어옴
# 1, 3, 5, ... 등의 index에는 수식(*,+,-)만 들어옴
for i in range(n):
    if i % 2 == 0: # 숫자가 들어오는 경우
        pass
    else: # 수식이 들어오는 경우
        if math_expression[i] == '+':
            answer += math_expression[i-1] + math_expression[i+1]
        elif math_expression[i] == '*':
            pass
        else: # '-'인 경우
            pass