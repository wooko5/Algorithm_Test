# 차례대로 곡을 연주한다는 점에서 DP를 사용하는 문제이다
# 곡의 개수가 N개, 볼륨의 최대값은 M
# DP를 이용해서 시간복잡도를 O(N*M)으로 해결가능
# 모든 볼륨에 대해 연주 가능 여부를 계산하기
N, S, M = map(int, input().split())
matrix = [[False for _ in range(M+1)] for _ in range(N+1)] # 항상 col, row 순서대로 이중배열 생성
matrix[0][S] = True
volume = list(map(int, input().split())) # 5, 3, 7이 들어간 상태
for i in range(1, N+1): # 1 2 3 
    for j in range(M+1): # 0 ~ 10
        if matrix[i-1][j] == True: 
            v = volume[i-1] # index 0 1 2
            if (j-v) > -1:
               matrix[i][j-v] = True
            if (j+v) < (M+1):
               matrix[i][j+v] = True
        else:
            continue

answer = -1
for index in range(M, -1, -1):
    if matrix[N][index]:
        answer = index
        break
print(answer)