n = int(input())
array = list(map(int, input().split()))
dp = [1]*n # 증가하는 부분수열의 길이를 담을 배열

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]: # 증가 부분수열임을 확인하는 조건
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp)) # 가장 긴 증가 부분수열 길이 출력

order = max(dp) # 가장 긴 증가 부분수열
temp = []
for i in range(n-1, -1, -1): # 역순으로 확인
    if dp[i] == order:
        temp.append(array[i])
        order -= 1
temp.reverse()
for i in temp:
    print(i, end=' ')