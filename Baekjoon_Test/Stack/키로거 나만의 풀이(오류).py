test_case = int(input())
cursor = 0
answer = []

for _ in range(test_case):
    password = list(input()) # 비밀번호 문자열로 입력

    for index in range(len(password)): # 비밀번호의 각 문자마다
        if '<' == password[index]:
            if cursor > 0:
                cursor -= 1
        elif '>' == password[index]:
            cursor += 1
        elif '-' == password[index]:
            del answer[len(answer)-1]
            cursor -= 1
        else:
            answer.insert(cursor, password[index])
            cursor += 1
    print(''.join(answer))