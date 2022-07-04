# 너무 어려워서 다시 한번 봐야겠음(2021.04.30)
from copy import deepcopy
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
answer = 10000

def value(array):
    return min([sum(i) for i in array])

def convert(array, query):
    (r, c, s) = query
    r, c = r-1, c-1
    new_array = deepcopy(array)
    
    for i in range(1, s+1):
        rr, cc = r - i, c + i # 계속 대각선으로 진행하기 때문 
        for j in range(4):
            for _ in range(i*2):
                rrr, ccc = rr + dx[j], cc + dy[j]
                new_array[rrr][ccc] = array[rr][cc]
                rr, cc = rrr, ccc
    return new_array

def dfs(array, query):
    global answer
    if sum(query) == K: # 쿼리를 모두 처리했다는 의미
        answer = min(answer, value(array))
        return 
    
    for i in range(K):
        if query[i]:
            continue
        new_arr = convert(array,  Q[i])
        query[i] = 1
        dfs(new_arr, query)
        query[i] = 0

dfs(A, [0 for _ in range(K)])
print(answer)