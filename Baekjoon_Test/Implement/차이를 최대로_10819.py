from itertools import permutations
n = int(input())
result = []
array = list(input().split())
arr = list(permutations(array))
for i in range(len(arr)):
    answer = 0
    for j in range(len(arr[i])-1):
        answer += abs(int(arr[i][j]) - int(arr[i][j+1]))
    result.append(answer)
print(max(result))