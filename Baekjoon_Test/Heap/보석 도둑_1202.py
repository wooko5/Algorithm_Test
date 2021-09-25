# 못 맞춘 이유: 최대힙과 최소힙을 이용하는건 알았지만 capable_gem같은 임시 배열을 생각하지 못함
# 못 맞춘 이유: for문보다 while문을 먼저 쓸 생각했음 
import heapq; import sys
N, K = map(int, input().split())
gem = []
result = 0 # 답이 될 숫자
capable_gem = [] # 현재 bag의 capacity보다 작은 모든 보석들
bag = []    

for _ in range(N):
    heapq.heappush(gem, list(map(int, sys.stdin.readline().split())))

for _ in range(K):
    heapq.heappush(bag, int(sys.stdin.readline()))

for _ in range(K):
    capacity = heapq.heappop(bag)

    while gem and capacity >= gem[0][0]: # 현재 bag의 capacity보다 이하인 모든 보석에 관하여
        heapq.heappush(capable_gem, -heapq.heappop(gem)[1]) # 무게를 제외한 값만 heappush하여 넣어준다(최대힙 구성)
    
    if capable_gem: # gem 최소보다는 작지만 넣을 수 있는 보석들은 있는 경우
        result -= heapq.heappop(capable_gem)
    
    elif not gem: # 남은 보석이 한 개도 없는 경우
        break
print(result)