import heapq # 기본적으로 최소힙(MIN HEAP)으로 생성 == 최소힙은 오름차순을 의미
n, m = map(int, input().split()) # n은 책의 개수, m은 한꺼번에 가져다 놓을 수 있는 책의 개수
array = list(map(int, input().split())) # 책의 위치에 대한 배열
positive =[] # 책의 위치가 양수인 배열
negative = [] # 책의 위치가 음수인 배열
result = 0
largest = max(max(array), -min(array)) # 절대값이 가장 큰 == 현재 위치(0)으로 부터 가장 먼 거리를 구하기
# 나중에 왕복거리를 구할 때, largest는 편도로 가겠끔 전체 왕복거리에서 largest만큼을 빼기 위함이다
for i in array: 
    if i > 0:
        heapq.heappush(positive, -i) # 최대 힙(MAX HEAP)을 위해 모든 원소를 음수로 구성(내림차순을 위해)
    else: # '모든 원소를 음수로 구성'하지 않고 그냥 넣으면 오름차순으로 삽입된다(최소힙)
        heapq.heappush(negative, i)

while positive:
    # 한번에 m개식 옮길 수 있으므로 m개씩 빼내기
    result += heapq.heappop(positive)
    for _ in range(m-1):
        if positive:
            heapq.heappop(positive)

while negative:
    # 한번에 m개식 옮길 수 있으므로 m개씩 빼내기
    result += heapq.heappop(negative)
    for _ in range(m-1):
        if negative:
            heapq.heappop(negative)

print(-result*2-largest) # result에 '-'를 붙이는 이유는 negative, positive 원소가 모두 음수이기 때문 