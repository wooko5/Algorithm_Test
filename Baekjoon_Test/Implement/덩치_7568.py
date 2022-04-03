matrix = []
answer = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    matrix.append([x, y])
for i in range(len(matrix)):
    count = 0
    for j in range(len(matrix)):
        if matrix[i][0] < matrix[j][0] and matrix[i][1] < matrix[j][1]:
            count += 1
    answer.append(count+1)
print(*answer)