def DFS(x, y):
    global count
    count += 1
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        current_x, current_y = dx + x, dy + y
        if current_x < 0 or current_x >= N or current_y < 0 or current_y >= N:
            continue
        if matrix[current_x][current_y] and not visited[current_x][current_y]:
            DFS(current_x, current_y)

N = int(input())
count = 0
answer = 0
result = []
visited = [[False]*N for _ in range(N)]
temp = []
matrix = [[] for _ in range(N)]
for _ in range(N):
    temp.append(list(input()))
for i in range(N):
    for j in range(N):
        matrix[i].append(int(temp[i][j]))
for i in range(N):
    for j in range(N):
        if matrix[i][j] and not visited[i][j]:
            DFS(i, j)
            answer += 1
            result.append(count)
            count = 0
print(answer)
result.sort()
for i in result:
    print(i)