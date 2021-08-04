from copy import deepcopy
def BFS(graph):
    global answer
    result = 0
    queue = []
    graph_copy = deepcopy(graph)
    
    for i in range(row):
        for j in range(col):
            if graph_copy[i][j] == 2:
                queue.append([i, j])
    
    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.pop(0)
        for dx, dy in distance:
            current_x, current_y = x + dx, y + dy
            if current_x >= 0 and current_y >= 0 and current_x < row and current_y < col: # row와 col을 반대로 넣고 돌렸었다 착각 ㄴㄴㄴ!
                if graph_copy[current_x][current_y] == 0:
                    graph_copy[current_x][current_y] = 2
                    queue.append([current_x, current_y])
    
    for i in graph_copy:
        for j in i:
            if j == 0:
                result += 1
    answer = max(answer, result)

def wall(count):
    if count == 3:
        BFS(matrix)
        return
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                wall(count+1)
                matrix[i][j] = 0


distance = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
row, col = map(int, input().split())
matrix = []
for _ in range(row):
    matrix.append(list(map(int, input().split())))
wall(0)
BFS(matrix)
print(answer)