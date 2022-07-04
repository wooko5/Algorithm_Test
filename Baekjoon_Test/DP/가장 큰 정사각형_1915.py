n, m = map(int, input().split())
matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for index, j in enumerate(list(map(int, list(input())))):
        matrix[i+1][index+1] = j # 원래 행+1, 열+1된 이중배열 생성

# dp[i][j] = (i, j)까지 왔을 때, 가장 큰 정사각형의 한 변의 길이
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if matrix[i][j]: # matrix의 원소가 0이 아니라면 dp에서 왼쪽, 왼쪽대각선쪽, 위쪽 원소중 가장 작은 것+1 
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            answer = max(dp[i][j], answer)
print(dp)
print(answer**2)