from copy import deepcopy
n = int(input())
array = list(map(int, input().split()))
dp = deepcopy(array) #dp[i]: i까지 왔을 때, 합의 최대

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]: # 증가 부분수열임을 확인하는 조건
            dp[i] = max(array[i]+dp[j], dp[i])
print(max(dp))