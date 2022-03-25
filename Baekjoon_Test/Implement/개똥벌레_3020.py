distance, height = map(int, input().split())
bottom = [0] * (height + 1)  # 석순
top = [0] * (height + 1)  # 종유석
answer = distance  # 파괴해야 하는 장애물의 최소값
count = 0  # 최소값이 나타나는 구간의 수

for i in range(distance):
    if i % 2 == 0: # 홀수번째 원소는 석순으로
        bottom[int(input())] += 1
    else: # 짝수번째 원소는 종유석으로
        top[int(input())] += 1

print(bottom)
print(top)
# 각 높이로 잘랐을 때 생기는 조각의 개수 
# i줄을 잘랐을 때 석순(bottom)은 높이가 i인 석순의 개수와 i+1이상의 석순의 개수
# i줄을 잘랐을 때 종유석(top)의 위치가 i인 석순의 개수와 i-1이하에 위치한 종유석의 개수
for i in range(height - 1, 0, -1): # 높이-1부터 1까지 역순으로 방해물 있는지 확인하기
    bottom[i] += bottom[i + 1]
    top[i] += top[i + 1]

print(bottom)
print(top)

for i in range(1, height + 1):
    if answer > (bottom[i] + top[height - i + 1]):
        answer = (bottom[i] + top[height - i + 1])
        count = 1
    
    elif answer == (bottom[i] + top[height - i + 1]):
        count += 1
print(answer, count)