test_case = int(input())
for _ in range(test_case):
    n = int(input()) # 아이들의 수
    c = list(map(int, input().split())) # 각 아이마다 받은 사탕 개수의 배열
    count = 0 # 얼마나 순환하는지 세기 위한 변수
    temp = [i for i in range(n)]

    for i in range(len(c)): # 선생님이 짝수 밖에 없는 사탕 개수를 만들기 위한 매직
        if c[i] % 2 == 1:
            c[i] += 1
    if len(set(c)) == 1: # 선생님이 조정 후, 사탕의 개수가 모두 고르게 배분된 경우
        print(0)
        continue
    
    while len(set(temp)) > 1:
        temp = [i for i in range(n)]
        for i in range(n): # 오른쪽으로 돌리면서 사탕 개수 조정
            if i == 0:
                temp[0] = c[0]//2 + c[-1]//2
            else: # 1, 2, 3, 4 
                temp[i] = c[i]//2 + c[i-1]//2
        count += 1
        
        for i in range(len(temp)): # 선생님이 짝수 밖에 없는 사탕 개수를 만들기 위한 매직
            if temp[i] % 2 == 1:
                temp[i] += 1
        c = temp
    print(count)