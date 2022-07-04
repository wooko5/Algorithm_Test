# 강사님: "사실 이 정도 수준의 문제는 안 나올 가능성이 크다. 즉, 매우 어렵다 그래도 알면 도움될꺼다"
# 이 문제가 어려운 이유는 dp를 어떤 형식으로 잡을지 감이 안 온다는 것 
# 여기서는 dp를 이중배열로 놓는다
# dp[i][j] = i에서 j까지 합치는데 드는 최소비용
# dp[i][j] = dp[i][k] + dp[k+1][j] + sum(array[i] ~ array[j])
def process():
    N = int(input()) # 파일의 개수
    array = [0] + list(map(int,input().split())) # 비용 배열, k개
    accumulator = [0 for _ in range(N+1)] # 누적합을 만들기 위한 배열, accumulator[i] = index 1부터 i까지 누적합 
    for i in range(1,N+1):
        accumulator[i] = array[i] + accumulator[i-1]
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(2, N+1): # 부분 파일의 길이를 구하는 반복문
        for j in range(1, N+2-i): # 시작점
            # 부분 파일의 길이만큼 가야하니깐 i를 넣는다
            # dp(j에서 k만큼 떨어진 곳까지 합) + dp(바로 다음 원소(j+k+1)부터 i 길이만큼 떨어진 곳)의 합
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] 
            for k in range(i-1)]) + (accumulator[j+i-1] - accumulator[j-1])# j부터 길이가 i인
            # i-1까지 하면 아무것도 더하지 않아서 0이 되므로 'i-2'로 해줘야한다
    print(dp[1][N]) 

for _ in range(int(input())):
    process()