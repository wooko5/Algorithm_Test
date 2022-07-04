n = int(input())
dp = [0]*31; dp[0] = 1; dp[2] = 3 # dp[0]이 1인 이유는 존재하지 않기 때문에 1인걸까????
for i in range(4, n+1):
    dp[i] = dp[i-2] * 3 # 2x3 도형을 가장 오른쪽에 두는 경우, 2x3 도형이 3개이기 때문에 *3을 해준다
    for j in range(4, i+1, 2): # n = 4부터는 새로운 도형이 추가된다. 
        dp[i] += dp[i-j] * 2 # 하지만 n이 4,6,8,10...일때 도형의 모양이 모두 다르기 때문에 각각 dp[i]에 더해준다.
print(dp[n]) 