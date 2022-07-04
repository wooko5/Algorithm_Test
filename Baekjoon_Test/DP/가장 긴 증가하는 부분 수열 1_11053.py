# LIS(가장 긴 증가하는 부분수열)문제는 무조건 DP문제임
# 수열의 크기가 n일때 시간복잡도는 O(n^2)으로 풀 수 있음
n = int(input())
array = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))