# 이중 배열을 시계 반대반향으로 돌리는 문제
def rotate():
    x, y = 0, 0
    n, m = row, col
    time = min(row, col) // 2 # 배열을 돌릴 테두리 갯수를 센다

    while time: # 북->동->남->서 방향으로 하나씩 회전을 하는데, range체크를 한다.
        cache = matrix[x][y]

        # 북쪽
        for i in range(m - 1):
            matrix[x][y + i] = matrix[x][y + i + 1]

        # 동쪽
        for i in range(n - 1):
            matrix[x + i][y + m - 1] = matrix[x + i + 1][y + m - 1]

        # 남쪽
        for i in range(m - 1):
            matrix[x + n - 1][y + m - 1 - i] = matrix[x + n - 1][y + m - 2 - i]

        # 서쪽
        for i in range(n - 1):
            matrix[x + n - 1 - i][y] = matrix[x + n - 2 - i][y]
        
        matrix[x + 1][y] = cache
        n -= 2 # 행, 안으로 들어가서 배열을 돌리기위해 일부러 2를 뺀다, 2를 빼는 것은 사각형의 양옆만 돌리기 때문
        m -= 2 # 렬, 행과 동일
        x += 1 # 가로
        y += 1 # 세로
        time -= 1 # 로테이트 횟수

def solution():
    for _ in range(rotate_count):
        rotate()
    for row in matrix:
        print(*row) # 리스트형식 없이 원소만 나옴

row, col, rotate_count = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(row)]
solution()