# 본 문제는 전형적인 '위상 정렬(Topology)' 문제
# 위상 정렬은 '순서가 정해져있는 작업'을 차례대로 수행해야할 때, 순서를 결정해주는 알고리즘이다
# 위상 정렬의 시간복잡도는 O(V+E)로 해결할 수 있습니다(V는 정점, E는 간선)
import heapq
N, M = map(int, input().split()) # N은 '전체 문제 개수', M은 '먼저 풀어야하는 문제의 개수'
matrix = [[] for _ in range(N + 1)] # (문제 개수+1)만큼의 행을 가진 이중 배열 생성
indegree = [0] * (N + 1) # 진입차수에 대한 배열
queue = []
answer = []

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x].append(y)
    indegree[y] += 1

for index in range(1, N + 1):
    if indegree[index] == 0:
        heapq.heappush(queue, index)

while queue: # 힙에 원소가 있을 때까지 무한 반복
    data = heapq.heappop(queue) # heap에서 pop()
    answer.append(data) # data를 정답 배열에 넣고
    for index in matrix[data]:  # data에서 이동할 수 있는 정점에 대해 확인하기
        indegree[index] -= 1 # index를 가리키는 진입차수를 -1 해준다 == 간선 제거
        if indegree[index] == 0: # 만약 진입차수가 0이라면 == 본인이 루트정점이라면
            heapq.heappush(queue, index) # heap에 그 숫자를 넣는다

for i in answer:
    print(i, end=' ')