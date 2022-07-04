import sys; sys.setrecursionlimit(100000)

def DFS(x, y, height): # 유기농 배추, 섬의 개수 문제랑 똑같다!!!
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 방향성에 대한 배열
    for dx, dy in directions:
        current_x, current_y = x + dx, y + dy
        if current_x >= N or current_x < 0 or current_y >= N or current_y < 0:
            continue # (current_x, current_y)를 index라 생각하면 쉽다. 0보다 작으면 안 되고, N-1보다 크면 오류(out of index)뜸 
        if matrix[current_x][current_y] > height and not visited[current_x][current_y]:
            DFS(current_x, current_y, height) # 내가 설정한 장마높이보다 크고, 방문하지 않은 구간이면 DFS재귀호출 

N = int(input())
matrix = []
answer = []

for _ in range(N): 
    matrix.append(list(map(int, input().split()))) # 높이는 1이상 100 이하의 정수이다.

biggest = max(map(max, matrix)) # 가장 큰 높이값
for height in range(1, biggest+1): # 높이 1부터 그 도심의 제일 큰 높이까지 장마가 온다고 생각한다
    visited = [[False]*N for _ in range(N)] # 방문한 지역을 표시하기 위한 matrix
    count = 0 
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > height and not visited[i][j]: # 처음에 'matrix[i][j] > height' 이걸 안 해서 틀렸음
                DFS(i, j, height) # 장마 높이(height)보다 더 높게 있는 빌딩의 높이 and 방문하지 않은 빌딩만 탐색
                count += 1
    answer.append(count)

if max(answer) == 0: # 와 이 경우를 생각못해서 계속 틀리다가 맞춤
    print(1) # 이 경우는 모든 지역의 높이가 1인데 장마가 안 온 경우 1이 나와야함
    # 근데 이게 없으면 max(answer)가 0으로 나와서 고생함
else: # 그렇지 않은 나머지 모든 경우
    print(max(answer))