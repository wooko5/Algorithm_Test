import sys; input = sys.stdin.readline
dp = [0]*1000001
for i in range(1, 1000001):
	for j in range(i, 1000001, i): # i만큼 건너뛰라는 것은 j = i*j랑 같은 의미이다
		dp[j] += i
	dp[i] += dp[i-1] # 누적합
for _ in range(int(input())):
	print(dp[int(input())])