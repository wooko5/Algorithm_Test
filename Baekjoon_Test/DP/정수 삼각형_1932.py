n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0: # 왼쪽 끝은 그대로 위의 원소를 더한다
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i])-1: # 오른쪽 끝은 그대로 위의 원소를 더한다
            triangle[i][j] += triangle[i-1][j-1]
        else: # 사이에 있는 원소는 위의 원소 중에 더 큰 걸로 더한다
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
print(max(triangle[n-1]))