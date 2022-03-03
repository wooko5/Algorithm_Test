import sys
input = sys.stdin.readline
MAX = 100000
CONSTRAINT = 1000000009
dp = [[0 for col in range(4)] for row in range(MAX+1)]
dp[1] = [0, 1, 0, 0] # dp[index][0]는 없다고 생각하자
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, MAX+1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % CONSTRAINT
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % CONSTRAINT
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % CONSTRAINT

t = int(input())
for i in range(t):
    n = int(input())
    print(sum(dp[n]) % CONSTRAINT)