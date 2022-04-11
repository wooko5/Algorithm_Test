def make_wall(): # 빈 공간에 벽을 세우는 함수
    for i in range(len(wall)):
        count = wall[i]
        for j in range(height-1, -1, -1):
            if count == 0:
                break
            matrix[j][i] = 2
            count -= 1

def make_rain(): # 벽과 벽 사이 빗물을 채우는 함수
    for i in range(height-1, -1, -1):
        start = 0
        end = 0
        count = 0
        for j in range(width):
            if matrix[i][j] == 2:
                count += 1
                if count % 2 == 1:
                    start = j
                    if matrix[i][j-1] == 0 and j > 0 and count > 1:
                        for k in range(end+1, start):
                            matrix[i][k] = 1
                else:
                    end = j
                    for k in range(start+1, end):
                        matrix[i][k] = 1

def solve(): # 빗물을 세는 정답출력 함수
    answer = 0
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 1:
                answer += 1
    return answer

height, width = map(int, input().split())
wall = list(map(int, input().split()))
matrix = [[0]*width for _ in range(height)]
make_wall()
make_rain()
print(solve())