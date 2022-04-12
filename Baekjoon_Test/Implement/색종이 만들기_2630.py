# 실버3의 간단한 재귀, Divide and Quenqor 문제였는데 못 풀었음
# 범위를 줄여서 재귀하면 되는건데 그걸 생각못함 ㅠㅅㅠ
# 재귀문제를 자주 풀어봐야겠다

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white = 0

def check(x, y, n): # 범위 내 색종이 색이 모두 같은지 확인하는 함수
    color = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != color:
                return False
    return True

def solve(x, y, n):
    global white, blue

    if check(x, y, n):
        if matrix[x][y]: # 1이면 파란색이고 True니깐 
            blue += 1
        else:
            white += 1
        return # 모두가 같은 색이니깐 여기서 끝내버리기
    else: # 종이 색깔이 같지 않다면
        n = n // 2 # 범위를 1/2로 줄여버리기
        solve(x, y, n)
        solve(x+n, y, n) # 아래
        solve(x, y+n, n) # 오른쪽
        solve(x+n, y+n, n) # 대각선 오른쪽 아래

solve(0, 0, n)
print(white)
print(blue)