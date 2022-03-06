#배열의 크기 * O(1)이다. (배열 하나당 O(1)의 시간복잡도를 가지므로)
#배열은 n+1이므로 시간복잡도는 O(n)

x = int(input())
dp = [0 for _ in range(x+1)]

for i in range(2, len(dp)):
    dp[i] = dp[i-1] + 1 # dp[i] = dp[i-1] + 1이 답이라고 전제
    if i % 2 == 0 and dp[i] > dp[i//2] + 1 : # 2로 나누어지고 and 기존값이 새로운 값보다 크다면
        dp[i] = dp[i//2] + 1 # 기존값을 새로운 값으로 갱신
    if i % 3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
print(dp)