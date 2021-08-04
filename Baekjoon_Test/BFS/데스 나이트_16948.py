def BFS(n, x, y, target_x, target_y):
    matrix = [[-1]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    matrix[x][y] = 0
    visited[x][y] = True
    queue = [(x,y)]

    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.pop(0) # 이걸 까먹어서 자꾸 무한루프에 빠졌음 ㅂㄷㅂㄷ!
        for dx, dy in distance:
            current_x, current_y = x + dx, y + dy
            if current_x >= 0 and current_y >= 0 and current_x < n and current_y < n:
                if visited[current_x][current_y] == False:
                    visited[current_x][current_y] = True
                    matrix[current_x][current_y] = matrix[x][y] + 1 # 이 개념이 진짜 어려운 것 같다
                    queue.append((current_x, current_y))
    
    print(matrix[target_x][target_y])
        
distance = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
n = int(input())
start_x, start_y, target_x, target_y = map(int, input().split())
BFS(n, start_x, start_y, target_x, target_y)