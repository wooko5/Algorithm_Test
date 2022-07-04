def rotate(p, ll, rl, ul, dl):
    x, y = p, p
    index = 0
    while True:
        x, y = x + dx[index], y + dy[index]
        if x == ul or x == dl or y == ll or y == rl:
            x, y = x - dx[index], y - dy[index]
            index += 1
            x, y = x + dx[index], y + dy[index]
        if x == p and y == p:
            return
        matrix[p][p], matrix[x][y] = matrix[x][y], matrix[p][p]

row, col, rotate_count = map(int, input().split())
matrix = [list(input().split()) for _ in range(row)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(min(row, col)//2):
    for _ in range(rotate_count % (2 * (row + col - 4 * i - 2))):
        rotate(i, i-1, col-i, i-1, row-i)
for e in matrix:
    print(*e)