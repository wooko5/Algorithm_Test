# 다시 봐야할 것 같다 너무 어려움(2021.04.30)
def new_array(n):
    return [[False for _ in range(10)] for _ in range(n)]

def dfs1(x, y):
    visited1[x][y] = True
    result = 1
    for dx, dy in directions:
        current_x, current_y = x + dx, y + dy
        if current_x < 0 or current_x >= n or current_y < 0 or current_y >= 10:
            continue
        if visited1[current_x][current_y] or matrix[x][y] != matrix[current_x][current_y]:
            continue
        result += dfs1(current_x, current_y)
    return result

def dfs2(x, y, value):
    visited2[x][y] = True
    matrix[x][y] = '0'
    for dx, dy in directions:
        current_x, current_y = x + dx, y + dy
        if current_x < 0 or current_x >= n or current_y < 0 or current_y >= 10:
            continue
        if visited2[current_x][current_y] or matrix[current_x][current_y] != value:
            continue
        dfs2(current_x, current_y, value)

def down():
    for i in range(10):
        temp = []
        for j in range(n):
            if matrix[j][i] != '0':
                temp.append(matrix[j][i])
        
        for j in range(n-len(temp)):
            matrix[j][i] = '0'
        
        for j in range(n-len(temp), n):
            matrix[j][i] = temp[j-(n-len(temp))]

n, k = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited1 = new_array(n)
visited2 = new_array(n)

while True:
    exist = False
    visited1 = new_array(n)
    visited2 = new_array(n)
    for i in range(n):
        for j in range(10):
            if matrix[i][j] == '0' or visited1[i][j]:
                continue
            result = dfs1(i, j) # 같은 거 개수 세기
            if result >= k:
                dfs2(i, j, matrix[i][j]) # 지우기
                exist = True 
    if not exist: # 지금까지 바뀌는 게 없었다면
        break
    down()

for i in matrix:
    print(''.join(i))