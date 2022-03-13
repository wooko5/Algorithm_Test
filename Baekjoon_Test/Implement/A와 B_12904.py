# S->T가 아닌 T->S를 생각해보자
# 1) 문자열 뒤의 A를 제거한다
# 2) 문자열 뒤의 B를 제거하고, 문자열을 뒤집는다
S = list(input())
T = list(input())
while len(T) != len(S): # 둘의 길이가 같을 때까지 반복한다
    if T[-1] == 'A': # 마지막 문자가 'A'인 경우, 마지막 문자를 pop()한다
        T.pop()
    elif T[-1] == 'B': # 마지막 문자가 'B'인 경우, 마지막 문자를 pop()하고 문자열을 뒤집는다
        T.pop()
        T = T[::-1]
if S == T:
    print(1)
else:
    print(0)