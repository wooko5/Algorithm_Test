S = input()
T = input()
C = len(T) - len(S) # 4 - 1 = 3
I = [[T]]

for _ in range(C):
    I.append([]) # I = [['ABBA'], []]
    for j in range(len(I[0])):
        if I[0][j][-1] == 'A': # T의 마지막 문자가 'A' 이면 
            I[1].append(I[0][j][:-1]) # T[ : 마지막 자리] 를 T[1] 에 삽입, 마지막 'A' 제외하고 삽입
        
        if I[0][j][0] == 'B': # T의 첫 문자가 'B' 이면 
            I[1].append(I[0][j][len(T)-1 : 0 : -1]) # T[T의 길이-1 : 0: -1] 를 I[1] 에 삽입, 첫번째 'B' 제외하고 뒤집어서 삽입
    del I[0] # I[0] 삭제해서 이전 단계 지움

if S in I[0]:
    print(1)
else:
    print(0)