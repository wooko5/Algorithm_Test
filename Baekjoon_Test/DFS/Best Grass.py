Row, Column = map(int, input().split())

def DFS(graph, start):
    visited, need_visit = list(), list()
    need_visit.append(start)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return len(visited)

matrix = [[] for _ in range(Row+1)]

for i in range(1, Row+1):
    arr = input()
    matrix[i].extend(arr)

print(DFS(matrix, '.'))