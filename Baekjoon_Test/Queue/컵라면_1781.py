import heapq
n = int(input())
matrix = []
queue = []
for _ in range(n): # 문제 정보를 입력받고, 데드라인을 기준으로 정렬함
    a, b = map(int, input().split())
    matrix.append([a,b])
matrix.sort()

for i in matrix:
    deadline = i[0] # 각 컵라면에 대한 데드라인 정보
    heapq.heappush(queue, i[1]) # 컵라면 보상 삽입
    if deadline < len(queue): # 만약 queue길이가 deadline을 초과하는 경우
        heapq.heappop(queue) # 같은 데드라인 컵라면 보상 중에 최소값을 제거
        # 같은 데드라인에는 1개의 컵라면 보상만 존재하게 된다
print(sum(queue))