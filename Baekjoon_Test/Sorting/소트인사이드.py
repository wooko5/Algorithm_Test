# 내가 한 풀이
N = input()
arr = []
for i in range(len(N)):
    arr.append(int(N[i]))
arr.sort(reverse=True)
for i in arr:
    print(i,end='')

#다른 풀이
array = input()
for i in range(9,-1,-1): # 9~0까지 역순으로 확인하기
    for j in array: 
        if int(j) == i: # 입력받은 숫자랑 같은 경우
            print(i,end='') # 그 숫자를 출력