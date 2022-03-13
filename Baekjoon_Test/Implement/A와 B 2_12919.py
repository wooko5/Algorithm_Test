# DFS를 통해 가지를 뻣어가며 백트랙킹을 하면 정답을 찾을 수 있다.

def DFS(string): # T -> S로 만들기 위한 DFS함수
    if len(string) == len(S):
        if string == S:
            print(1)
            exit(0)
        return
    
    if string[0] == 'B': # T의 첫번째 문자가 'B'라면 
        string = string[::-1] # 문자열을 전체 뒤집고 
        string.pop() # 마지막 문자('B')를 없앤다
        DFS(string) # 재귀함수 호출
 
        # 백트랙킹을 위한 초기화.
        string.append('B') # 다시 B를 맨 뒤에 삽입하고
        string = string[::-1] # 기존의 뒤집혀진 문자열을 다시 원상태로 복구
    
    if string[-1] == 'A': # T의 마지막 문자가 'A'라면 
        string.pop() # 마지막 문자('A')를 없앤다
        DFS(string)

        # 백트랙킹을 위한 초기화.
        string.append('A') # 다시 'A'를 붙여줌

S = list(input())
T = list(input())
DFS(T)
print(0)