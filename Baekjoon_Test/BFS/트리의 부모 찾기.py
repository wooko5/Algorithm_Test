from collections import deque
N = int(input())
matrix = [[] for _ in range(N+1)] 
parents = [0]*(N+1) # 부모노드에 대한 배열 parents 생성
parents[1] = 1 #1이 루트노드라서 1의 부모노드는 자기 자신이다

for _ in range(N-1):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

queue = deque([1]) # 큐 생성 # [1]
while queue: # bfs방식으로 부모노드에 접근함
    node = queue.popleft() # 큐의 가장 첫번째 요소 추출
    for child in matrix[node]: # matrix[node]에 연결된 child 노드 순회
        if not parents[child]: # 만약에 child가 parents에 없다면 == 한번도 부모 노드를 방문한 적 없다면
            parents[child] = node # 부모노드에 현재 node값을 저장한다
            queue.append(child)

for node in parents[2:]: # 2번째 노드부터 마지막 노드까지 부모노드를 출력, [0,,0,0,0,0,0,] --> [1,23,4]
    print(node)