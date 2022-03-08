n, m = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)] # 0으로 채워진 (n+1)행 (m+1)렬 생성 

for i in range(1, n+1):
    for j in range(1, m+1): # dp 배열의 좌와 우를 matrix배열 원소와 더하고, dp배열의 왼쪽 대각선 원소를 뺀다 
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + matrix[i-1][j-1] - dp[i-1][j-1] 

# dp[i][j] = (1,1)부터 (i, j)까지의 부분합을 의미
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]) # 교집합이라고 생각해보자