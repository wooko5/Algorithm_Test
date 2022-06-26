N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)):
    print(arr[i])