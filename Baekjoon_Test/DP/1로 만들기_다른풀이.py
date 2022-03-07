# 80%까지는 맞는데 틀림 ㅠㅠ 
import math
x = int(input())
dp = [0]*(x+1)
for i in range(2, len(dp)):
    if math.log(i,2) == int(math.log(i,2)):
        dp[i] = int(math.log(i,2))
    elif math.log(i,3) == int(math.log(i,3)):
        dp[i] = int(math.log(i,3))
    else: # 2와 3의 제곱이 아닌 수: ex) 5, 6, 7 ....
        if i % 3 == 0:
            dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)
        elif i % 2 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
        else:
            dp[i] = dp[i-1] + 1
print(dp)