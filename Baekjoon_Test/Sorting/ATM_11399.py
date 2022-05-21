import sys; input = sys.stdin.readline; n = int(input())
array = list(map(int, input().split()))
array = sorted(array)
answer = 0
for i in range(len(array)):
    temp = 0
    for j in range(i+1):
        temp += array[j]
    answer += temp
print(answer)