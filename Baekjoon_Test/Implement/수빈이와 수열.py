n = int(input())
array = list(map(int, input().split()))
print(array[0], end=' ')
for i in range(1, len(array)):
    print(array[i]*(i+1)-array[i-1]*i, end=' ')