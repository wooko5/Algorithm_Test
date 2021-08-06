from itertools import combinations
n, s = map(int, input().split())
array = list(input().split())
count = 0
temp = 0
for i in range(1, n+1):
    for arr in list(combinations(array, i)):
        for j in arr:
            temp += int(j)
        if temp == s:
            count += 1
        temp = 0
print(count)