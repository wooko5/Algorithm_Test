sentence = input()
temp = ''
check = False

for i in sentence:
    if i == ' ': # 공백이 문장에 존재하는 경우
        if not check: # 'check == False'랑 같은 의미, 꺽새('<', '>')가 닫혀있다는 의미
            print(temp[::-1], end=' ')
            temp = '' # 역순으로 출력하면 음절을 다 사용했기에 다시 초기화해줌
        else: # 꺽새('<', '>')가 열려있다는 의미
            print(' ', end='')
    
    elif i == '<': # '<' or '>'가 문장에 존재하는 경우
        check = True
        print(temp[::-1] + '<', end='')
        temp = ''
        
    elif i == '>':
        check = False
        print('>', end='')
    
    else: # 알파벳과 숫자만 문장에 존재하는 경우
        if check: # 꺽새('<', '>')가 열려있다는 의미
            print(i, end='')
        else:
            temp += i
print(temp[::-1])