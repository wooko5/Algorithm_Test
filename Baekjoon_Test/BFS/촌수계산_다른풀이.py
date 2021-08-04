import sys
input = sys.stdin.readline
N = int(input()) # 전체 사람의 수 == 전체 노드의 개수
A, B = map(int, input().split()) # 노드 A와 B
E = int(input()) # 전체 엣지의 개수
family = [[] for _ in range(N+1)] # 촌수관계를 알려주는 그래프
visited = [0]*(N+1) # 방문노드 배열
count = 0 # 촌수를 알기위한 답

for _ in range(E):
    u, v = map(int, input().split())
    family[u].append(v)
    family[v].append(u)

def BFS(graph, node):
    need_visit = [node]
    while need_visit:
        node = need_visit.pop(0)
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                need_visit.append(i)

BFS(family, A)
print(visited[B] if visited[B] else -1)