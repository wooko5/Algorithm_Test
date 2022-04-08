import sys
input = sys.stdin.readline
N, SUM = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
ans = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            answer.append(arr[i]+arr[j]+arr[k])
for i in answer:
    if i <= SUM:
        ans.append(i)
print(max(ans))