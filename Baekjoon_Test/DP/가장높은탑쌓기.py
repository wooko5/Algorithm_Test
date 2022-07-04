test_case = int(input())
stones = [0]*(test_case+1) # 번호가 i인 벽돌을 가장 아래에 두었을 때 최대 높이를 저장하는 배열
matrix = [(0,0,0,0)] # 벽돌 번호(1부터 시작), 벽돌 밑면 넓이, 높이, 무게를 넣기 위해 0으로 초기화 

for index in range(1, test_case + 1):
    area, height, weight = map(int, input().split())
    matrix.append((index, area, height, weight)) # 벽돌에 대한 정보를 가진 이중배열 생성

matrix = sorted(matrix, key=lambda x:x[3]) # '무게'를 기준으로 정렬함

for i in range(1, test_case+1): # 비교되어지는 대상
    for j in range(0, i): # 비교하는 대상
        if matrix[i][1] > matrix[j][1]: # 벽돌i가 벽돌j의 넓이보다 더 크면 
            stones[i] = max(stones[i], stones[j]+matrix[i][2]) # 벽돌을 쌓았을 때 
            #최대높이는 '현재 벽돌 높이 or 전 벽돌 높이 + 높이'중에 더 큰 거 

max_value = max(stones) # 벽돌을 쌓았을 때 제일 큰 높이
answer = []

while test_case != 0: 
    if max_value == stones[test_case]: # 최대높이가 현재 배열의 값과 같다면
        answer.append(matrix[test_case][0]) # 정답 배열에 높이에 해당하는 벽돌번호 삽입
        max_value -= matrix[test_case][2] # 최대 높이는 현재 벽돌의 높이를 뺀 값으로 갱신
    test_case -= 1 # 역순으로 찾기

answer.reverse()
print(len(answer))
for i in answer:
    print(i)