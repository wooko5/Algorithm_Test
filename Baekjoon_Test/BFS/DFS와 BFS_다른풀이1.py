def DFS(graph, start): 
    visited = []
    need_visit = [start] 
    while need_visit: 
        node = need_visit.pop() 
        if node not in visited: 
            visited.append(node) 
            need_visit += reversed(graph[node]) 
    return visited

def BFS(graph, start): 
    visited = []
    need_visit = [start] 
    while need_visit:
        node = need_visit.pop(0) 
        if node not in visited: 
            visited.append(node) 
            need_visit += graph[node] 
    return visited

N, M, V = map(int, input().split()) 
matrix = [[]*(N+1) for _ in range(N+1)] 

for i in range(1, M+1): 
    x, y = map(int, input().split()) 
    matrix[x].append(y) 
    matrix[y].append(x) 

for index in range(len(matrix)): 
    matrix[index].sort() 
    
print(' '.join(list(map(str,DFS(matrix, V))))) 
print(' '.join(list(map(str,BFS(matrix, V)))))