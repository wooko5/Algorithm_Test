from bisect import bisect # 기존의 dp를 이용한 LIS방식에서 이분탐색을 이용하면 효율성이 올라감
n = int(input())
array = list(map(int, input().split()))
dp = [array[0]] # 첫번째 원소 넣기
for i in range(1, n):
    if array[i] > dp[-1]:
        dp.append(array[i])
    else:
        index = bisect(dp, array[i]) # dp에 원하는 원소가 없으면 0을 반환
        dp[index] = array[i] # 맨 앞 원소를 갱신
print(dp)
print(len(dp))