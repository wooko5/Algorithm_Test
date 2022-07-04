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
            if (j-volume[i-1]) > -1:
                matrix[i][j-volume[i-1]] = True # 순서대로 volume의 5, 3, 7을 넣어서 연산한다
            if (j+volume[i-1]) < (M+1):
                matrix[i][j+volume[i-1]] = True
        else:
            continue

answer = -1
for index in range(M, -1, -1): # matrix의 마지막 음악의 끝 번호부터 역순으로 True를 찾고
    if matrix[N][index]: # 찾았다면 
        answer = index # answer에 true가 있는 index을 복사해서
        break
print(answer) # 출력