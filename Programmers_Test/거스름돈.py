
"""
def solution(n, money): # 하다가 실패한 코드
    array = [[1 for _ in range(n+1)] for _ in range(len(money))]
    for i, coin in enumerate(money):
        for j in range(n+1):
            if coin <= j and i-1 >= 0 and j-coin >= 0:
                array[i][j] = (array[i-1][j] + array[i][j-coin]) % 1000000007
            else:
                array[i][j] = array[i-1][j]
    return array[-1][-1]
"""


"""
dp문제 잼병임을 다시 한번 입증했다
정말 지금봐도 뭔 소리인가 싶다 
다시 한번 풀어야한다 꼭 후우,,,,
2021.07.26
"""
def solution(n, money): 
    dp = [1] + [0] * n 
    for coin in money: 
        for i in range(coin, n + 1): 
            if i >= coin: 
                dp[i] += dp[i - coin] 
    return dp[n] % 1000000007


n = 5
money = [1, 2, 5]
print(solution(n, money))