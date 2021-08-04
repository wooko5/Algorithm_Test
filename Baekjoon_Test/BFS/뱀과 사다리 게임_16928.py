from collections import deque
def BFS(node):
    queue = deque([node])
    visited[node] = 0
    while queue:
        node = queue.popleft()
        for i in range(1, 7):
            number = node + i
            if number > 100: # 주사위를 굴러서 옮길 자리가 100을 넘어가면 안됨
                continue
            j = matrix[number] # j는 주사위를 굴려서 우리가 도착할 지점
            if visited[j] == -1 or visited[j] > matrix[j]+1: # 한번도 도착해본 적이 없거나 
                queue.append(j)
                visited[j] = visited[node]+1

n, m = map(int, input().split())
matrix = [i for i in range(101)]
visited = [-1]*101

for _ in range(n):
    x, y = map(int, input().split())
    matrix[x] = y
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x] = y

BFS(1)
print(matrix)
print(visited[100])