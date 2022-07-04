computer = int(input())
networks = int(input())
matrix = [[] for _ in range(computer+1)]
visited = [False]*(computer+1)
count = 0

for _ in range(networks):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

def DFS(start):
    global count
    count += 1
    visited[start] = True
    for node in matrix[start]:
        if not visited[node]:
            DFS(node)
DFS(1)
print(count-1)