import sys
# 문제의 요구사항은, 정렬된 센서들을 최대 station개의 영역으로 나누는 것과 동일하다
sensor = int(input())
station = int(input())

# 집중국의 개수가 sensor 이상일 때 
if station >= sensor:
    print(0) # 각 센서의 위치에 집중국을 설치하면 되므로 0이 된다
    sys.exit()

# 각 센서를 오름차순 정렬하기
array = list(map(int, input().split()))
array.sort()

# 각 센서 사이의 거리를 계산하기
distance = []
for i in range(len(array)-1):
    distance.append(abs(array[i]-array[i+1]))

# 가장 거리가 먼 순서대로 station-1개의 연결고리를 제거하기 or 내림차순 정렬 후 제거도 가능하다
for _ in range(station-1):
    distance.remove(max(distance))
print(sum(distance))