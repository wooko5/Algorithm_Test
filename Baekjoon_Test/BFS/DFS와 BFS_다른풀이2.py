from collections import deque
def DFS(graph, start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not(visited[i]):
            DFS(graph, i)

def BFS(graph, start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            for i in graph[node]:           
                queue.append(i)


N, M, V = map(int, input().split()) 
matrix = [[] for _ in range(N+1)] 

for _ in range(M): 
    x, y = map(int, input().split()) 
    matrix[x].append(y) 
    matrix[y].append(x) 

for key in matrix:
    key.sort()

visited = [False]*(N+1)
DFS(matrix, V)
print('')
visited = [False]*(N+1)
BFS(matrix, V)