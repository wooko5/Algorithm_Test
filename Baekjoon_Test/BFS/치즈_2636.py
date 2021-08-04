def bfs(cheese):
    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.pop(0)

        for dx, dy in distance:
            current_x = x + dx
            current_y = y + dy

            if 0 <= current_x < n and 0 <= current_y < m and not visited[current_x][current_y]:
                visited[current_x][current_y] = True

                if matrix[current_x][current_y] == 1: # 치즈 가장자리를 만나면
                    matrix[current_x][current_y] = 2 # 2로 갱신해주기
                    cheese -= 1 # 치즈의 전체 개수에서 -1 해주기
                
                else:
                    queue.append([current_x, current_y]) # 치즈가 아니라면 큐에 넣고 재탐색
    return cheese # 남은 치즈 개수 반환

def clean():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2: # 치즈가 있다면 
                matrix[i][j] = 0 # 0으로 갱신

distance = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
matrix = []
queue = []
cheese = 0
time = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1: 
            cheese += 1 # 치즈의 전체 개수 

temp = cheese # 얘를 지우면 NameError가 남 
while cheese != 0:
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.append([0, 0])
    visited[0][0] = True
    cheese = bfs(cheese) # 현재 치즈의 남은 개수를 반환

    if cheese != 0: # 치즈가 1개라도 존재한다면
        temp = cheese # 현재 남은 치즈 개수를 temp로 갱신함

    time += 1 # 큐에 남은 원소들이 다 소진되면 1단계가 끝났다고 생각하고 +1해줌
    clean() # 2로 된 원소들을 모두 0으로 바꾸기 -> 다시 탐색해야하기 때문

print(time) # 모두 0으로 만들기 위한 단계의 수
print(temp) # 마지막 단계의 치즈개수 