T = int(input())
for i in range(T):
    data = list(map(int, input().split()))
    data.sort()
    print(data[-3])