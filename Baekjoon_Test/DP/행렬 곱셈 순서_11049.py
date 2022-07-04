# 이해가 가지 않는다 ㅠㅠㅠ 다음에 다시 한번 풀어보자
import sys; input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        # j = 첫행렬위치, x = 마지막 행렬 위치
        x = j + i 
        dp[j][x] = 2 ** 32

        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])
# dp[첫행렬 위치][k] + dp[k+1][마지막 행렬 위치] + matrix[첫행렬 위치][0] * matrix[k][1] * matrix[마지막행렬 위치][1]
print(dp[0][n - 1])