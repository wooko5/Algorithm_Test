from copy import deepcopy
# 너무 어렵다 이건 다시 풀어보자! 
dx = [0, -1, 0, 1] # 좌우 방향성을 알려주는 배열
dy = [-1, 0, 1, 0] # 상하 방향성을 알려주는 배열

def BFS(i, j, matrix): # bfs이용해 바이러스 퍼뜨림
    need_visit = []
    need_visit.append([i, j])
    while need_visit:
        x, y = need_visit.pop(0)
        for direction in range(4): # 4인 이유는 좌, 우, 상, 하 방향성이 4개라서
            xx, yy = x + dx[direction], y + dy[direction]
            if 0 <= xx < N and 0 <= yy < M and matrix[xx][yy] == 0:
                matrix[xx][yy] = 2
                need_visit.append([xx, yy])

def sol(ix, iy, jx, jy, kx, ky):
    matrix_copy = deepcopy(matrix_original)
    matrix_copy[ix][iy] = 1
    matrix_copy[jx][jy] = 1
    matrix_copy[kx][ky] = 1
    for i in range(N):
        for j in range(M):
            if matrix_copy[i][j] == 2:
                BFS(i, j, matrix_copy)
    cnt = sum(i.count(0) for i in matrix_copy)
    return cnt

N, M = map(int, input().split())
matrix_original = [list(map(int, input().split())) for _ in range(N)]
matrix_copy = deepcopy(matrix_original)
result = 0

#좌표가 아닌 순서로 보고 3개를 고른 다음, 다시 좌표값으로 계산해줌
for i in range(N*M):
    for j in range(i+1, N*M):
        for k in range(j+1, N*M):
            ix, iy, jx, jy, kx, ky = i//M, i%M, j//M, j%M, k//M, k%M
            if matrix_original[ix][iy] == 0 and matrix_original[jx][jy] == 0 and matrix_original[kx][ky] == 0:
                result = max(result, sol(ix, iy, jx, jy, kx, ky))
print(result)