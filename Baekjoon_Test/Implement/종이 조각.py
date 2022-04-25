N, M = map(int, input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
result = 0

for i in range(N):
    num = input()
    for j in range(len(num)):
        matrix[i][j] = int(num[j])

if N == 1 and M == 1:
    print(matrix[0][0])

for i in range(N):
    result += sum(matrix[i])
    for j in range(M):
        sum(matrix[i][j])
        