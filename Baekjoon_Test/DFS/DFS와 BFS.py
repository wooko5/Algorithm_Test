import sys
input = sys.stdin.readline
N, M, V = map(int, input().split()) # N은 노드의 개수, M은 엣지의 개수, V는 탐색을 시작할 노드번호
matrix = [[0]*(N+1) for _ in range(N+1)] # N+1의 행렬 길이를 갖는 행렬 만들기
visited = [0]*(N+1)
answer = []
for _ in range(M):
    A, B = map(int, input().split())
    matrix[A][B] = matrix[B][A] = 1 # 노드와 엣지의 상태를 인접행렬로 만들기

def DFS(graph, node):
    visited[node] = 1 # 이미 방문한 노드를 1로 저장
    print(node, end=' ')
    for index in range(1,N+1):
        if visited[index] == 0 and graph[node][index] == 1:
            DFS(graph,index)

def BFS(graph, node):
    need_visit = [node] # 방문예정인 노드 저장
    visited[node] = 0 # 이미 방문한 노드를 0으로 저장
    
    while need_visit:
        node = need_visit.pop(0)
        print(node, end=' ')
        for index in range(1, N+1):
            if visited[index] == 1 and graph[node][index] == 1:
                need_visit.append(index)
                visited[index] = 0
DFS(matrix,V)
print('')
BFS(matrix,V)