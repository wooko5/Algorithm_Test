row, col = map(int, input().split())
farm = [list(input()) for _ in range(row)]
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
check = False

for i in range(row):
    for j in range(col):
        if farm[i][j] == 'W':
            for dx, dy in directions:
                current_x, current_y = i + dx, j + dy
                if current_x < 0 or current_x >= row or current_y < 0 or current_y >= col:
                    continue
                if farm[current_x][current_y] =='S':
                    check = True

if check:
    print(0)
else:
    print(1)
    for i in range(row):
        for j in range(col):
            if farm[i][j] not in 'SW':
                farm[i][j] = 'D'
    for i in farm:
        print(''.join(i))