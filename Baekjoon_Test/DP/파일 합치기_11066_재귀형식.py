def process():
    global accumulator, dp
    N, array = int(input()), list(map(int, input().split()))
    accumulator = [0 for _ in range(N+1)] # 누적합을 위한 배열
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)] # dp를 위한 이중배열
    for i in range(1, N+1):
        accumulator[i] = accumulator[i-1] + array[i-1]
    print(cost(1, N))

def cost(i, j): # i부터 j까지 최소비용합 구하는 함수
    global accumulator, dp
    if i == j: # 둘이 같으면 구할 필요없고 0임
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    
    for k in range(i, j):
        temp = cost(i,k) + cost(k+1, j) + accumulator[j] - accumulator[i-1]
        
        if dp[i][j] == 0 or dp[i][j] > temp:
            dp[i][j] = temp
    return dp[i][j]

accumulator, dp = 0, 0
for _ in range(int(input())):
    process()