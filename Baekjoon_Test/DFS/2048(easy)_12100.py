# 단순하게 상하좌우로 생각하지 말고, 판을 돌려서(90, 180, 270도) 한번에 다 밀어준다고 생각하자 
# dfs 문제 중 굉장히 어려운 수준이므로 나중에 bfs로 가능한지 알아보고 안 보고 짤 수 있을 정도로 외우자
from copy import deepcopy
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def convert(array, n):
    array_new = [i for i in array if i] # 배열에 자연수만을 남기기 위한 초기화 
    
    for i in range(1, len(array_new)):
        if array_new[i-1] == array_new[i]: # 바로 옆의 숫자가 같은 경우
            array_new[i-1] *= 2 # 합치면 2곱하기 
            array_new[i] = 0 # 나머지는 빈칸으로 만들기 위해 0
    
    array_new = [i for i in array_new if i] # 배열에 양수만을 남기기 위한 초기화 
    return array_new + [0] * (n-len(array_new))


def rotate90(board, n):
    matrix_new = deepcopy(board)
    for i in range(n):
        for j in range(n):
            matrix_new[j][n-i-1] = board[i][j] # 이렇게 하면 90도 돌아간 이중배열 생성됨, 암기하자
    return matrix_new


def dfs(n, board, count):
    result = max([max(i) for i in board]) # 보드에서 가장 큰 숫자
    if count == 0:
        return result
    
    for _ in range(4): # 상하좌우로 한번씩 다 밀면서 
        # matrix_copy = matrix # 이런 식으로 하면 주소값만 이전되므로 원본훼손 가능성 존재
        # matrix_copy = deepcopy(matrix) # 이렇게 해야 복사된 다른 배열 생성
        X = [convert(i, n) for i in board]
        if X != board: # 기존값과 다르다면
            result = max(result, dfs(n, X, count-1))
        board = rotate90(board, n) # 한번 돌릴 때마다 90도씩
    return result 

print(dfs(n, matrix, 5))