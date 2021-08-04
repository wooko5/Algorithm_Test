N, E = map(int, input().split())
matrix = [[] for _ in range(N+1)] # 노드들의 연결상태를 나타내는 matrix 생성
visited = [0]*(N+1) # 방문한 노드들의 상태를 나타내는 visited 생성
count = 0

for i in range(E): # 노드들의 연결상태를 나타내는 matrix에 정보를 넣는다
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

def DFS(graph, node): # 기존에 배운 while문 dfs를 못 쓰는 것은 visited[] 방문배열이 없기 때문이다
    visited[node] = 1 # 방문순서가 중요하다면 예전 우리가 쓰던거!, 그게 아니라면 이걸 쓰자
    # 만약 노드의 방문순서를 알고싶다면 print(node, end=' ')로 하면 됨
    for index in graph[node]:
        if visited[index] == 0:
            DFS(graph, index)

def BFS(graph, start):
    need_visit = [start]

    while need_visit:
        node = need_visit.pop(0)
        for i in graph[node]: # matrix를 append로 했으니 가능함
            if visited[i] == 0:
                need_visit.append(i)
                visited[i] = 1

for i in range(1, N+1): 
    if visited[i] == 0: # not visited[i]
        BFS(matrix, i)
        count += 1
print(count)


# 이런 방식으로 푸는 것도 가능함 # 
graph = [[0]*(N+1) for _ in range(N+1)] # 이런 방식도 가능함

for i in range(E): # 노드들의 연결상태를 나타내는 matrix에 정보를 넣는다
    u, v = map(int, input().split())
    matrix[u][v] = matrix[v][u] = 1

def dfs(graph, node):
    visited[node] = 1
    for index in range(N+1):
        if visited[index] == 0 and graph[node][index] == 1:
            DFS(graph, index)