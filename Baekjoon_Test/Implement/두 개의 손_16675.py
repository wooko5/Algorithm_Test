game = list(input().split())
check_ms = False
check_tk = False

for i in range(2): # 민성이가 이기는 경우의 수
    if game[i] == 'R':
        if game[2] == 'S' and game[3] == 'S':
            check_ms = True
    elif game[i] == 'S':
        if game[2] == 'P' and game[3] == 'P':
            check_ms = True
    elif game[i] == 'P':
        if game[2] == 'R' and game[3] == 'R':
            check_ms = True

for i in range(2,4): # 태경이가 이기는 경우의 수
    if game[i] == 'R':
        if game[0] == 'S' and game[1] == 'S':
            check_tk = True
    elif game[i] == 'S':
        if game[0] == 'P' and game[1] == 'P':
            check_tk = True
    elif game[i] == 'P':
        if game[0] == 'R' and game[1] == 'R':
            check_tk = True

if check_ms:
    print('MS')
elif check_tk:
    print('TK')
else: # 승부의 세계에서 둘다 이기는 경우는 없기 때문에, 이 경우는 서로 이기질 못할 경우이다(서로 비기거나 질 경우)
    print('?')