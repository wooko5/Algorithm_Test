# pypy3로 제출해야 성공함
# 간선의 숫자가 너무 많기 때문에 dfs보다 bfs를 사용해야함

from collections import deque
def bfs(start):
    queue = deque([start])
    visited = [False]*(N+1)
    visited[start] = True
    count = 1
    while queue:
        node = queue.popleft()
        for i in matrix[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count 

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
answer = [0]

for _ in range(M):
    y, x = map(int, input().split())
    matrix[x].append(y)

for i in range(1, N+1):
    answer.append(bfs(i))

for i in range(1, len(answer)):
    if answer[i] == max(answer):
        print(i , end=' ')