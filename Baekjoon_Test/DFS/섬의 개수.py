import sys; sys.setrecursionlimit(100000)
# 그냥 제출하면 파이썬은 기본 재귀함수 호출이 1000번이라 불가능하다 
# 고로 재귀함수 호출을 변경하든지 아니먄 bfs로 풀어라
# 난 dfs가 시간복잡도에서 우수할 것이라 생각해서 이렇게 풀었음
def dfs(x, y):
    visited[x][y] = True # 8방향 모두 접근해야하므로, 유기농 배추(1012번)과 매우 유사한 문제이다
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)] # 총 8방향
    for dx, dy in directions:
        current_x, current_y = dx+x, dy+y
        if current_x < 0 or current_x >= row or current_y < 0 or current_y >= col:
            continue
        if matrix[current_x][current_y] and not visited[current_x][current_y]:
            dfs(current_x, current_y)

while True:
    col, row = map(int, input().split())
    if col == 0 and row == 0: # 0, 0 이면 무한루프를 끝내도록 하자 
        break
    matrix = [] 
    visited = [[False]*col for _ in range(row)]
    count = 0
    
    for _ in range(row): # (row, col) 행렬 생성
        matrix.append(list(map(int, input().split())))
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] and not visited[i][j]: # 방문하지 않은 원소에 접근하고 
                dfs(i, j) 
                count += 1 
    print(count) 