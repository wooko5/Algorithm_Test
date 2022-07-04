from collections import deque
array = []

def bfs(x, y, board, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
 
    while queue:
        x, y = queue.popleft()
        print(x, y, board[x][y])
        if board[x][y] == 3:
            array.append(count)
            count = 0
            break
        for i in range(4):
            current_x = x + dx[i]
            current_y = y + dy[i]
 
            if 0 <= current_x < len(board) and 0 <= current_y < len(board[0]):
                if board[current_x][current_y] == 0 and not visited[current_x][current_y]:
                    visited[current_x][current_y] = True
                    count += 1
                    queue.append((current_x, current_y))
                    
def solution(board, c):
    answer = 0
    # 0은 빈 곳, 1은 바위길, 2는 로봇, 3은 도착지
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                bfs(i, j, board, visited)
                current_x, current_y = i, j
            elif board[i][j] == 3:
                position_x, position_y = i, j
    
    answer = abs(position_x - current_x) + abs(position_y - current_y)
    if position_x == current_x or position_y == current_y:
        answer += (answer - 1) * c
    print(array)
    return answer

board = [ [0,0,0,0,2,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0,1,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,3,0,0,0,1,0]]
c = 1
print(solution(board, c))