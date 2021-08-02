def BFS(x, y): # 안전 영역, 유기농 배추 문제와 매우 유사함
    global answer
    queue = set() # 알파벳이 동일한 경우는 한 번만 계산하기 위해 set()자료형을 이용함
    queue.add((x, y, matrix[x][y]))

    while queue:
        x, y, alpha = queue.pop()
        answer = max(answer, len(alpha)) # 가장 긴 이동거리를 저장
        for i in range(4): # 상하좌우 4방향으로 이동하는 것을 확인
            current_x = dx[i] + x
            current_y = dy[i] + y
            if  current_x >= row or current_x < 0 or current_y >= col or current_y < 0:
                continue
            if matrix[current_x][current_y] not in alpha: # 이동할 장소가 한 번도 방문해본 적 없는 알파벳이면 방문함
                queue.add((current_x, current_y, alpha + matrix[current_x][current_y]))

row, col = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
matrix = []
answer = 0

for _ in range(row):
    matrix.append(list(input()))

BFS(0, 0) # 항상 가장 왼쪽 상단에서 출발하기 때문에 (0, 0)이 출발점이다
print(answer)