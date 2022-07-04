import bisect # 가장 긴 증가하는 부분 수열 3과 코드가 동일
n = int(input())
array = list(map(int, input().split()))
dp = [array[0]] # array의 첫번째 원소
for i in range(1, n):
    if array[i] > dp[-1]: # 현재값이 부분수열의 최대값보다 큰 경우
        dp.append(array[i]) 
    else: # 현재값이 부분수열의 어느 부분에 해당되는지 index로 확인
        index = bisect.bisect_left(dp, array[i]) # 같은 값이면 제일 왼쪽(앞)에 있는 index를 반환하는 이분탐색
        dp[index] = array[i] # 해당 위치의 값을 갱신
print(len(dp))