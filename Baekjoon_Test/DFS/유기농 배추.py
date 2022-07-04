import sys; sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        current_x, current_y = x + dx, y + dy
        if current_x >= N or current_x < 0 or current_y >= M or current_y < 0:
            continue
        if matrix[current_x][current_y] and not visited[current_x][current_y]:
            dfs(current_x, current_y)        

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    visited = [[False]*M for _ in range(N)]
    matrix = [[0]*M for _ in range(N)]
    answer = 0

    for _ in range(K):
        y, x = map(int, input().split())
        matrix[x][y] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer) 