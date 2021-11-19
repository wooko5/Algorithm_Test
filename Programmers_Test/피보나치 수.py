def fibo(number):
    dp = [0]*100001
    dp[1] = 1
    for i in range(2, number+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[number] 
    
def solution(n):
    return fibo(n) % 1234567

n = 100000
print(solution(n))