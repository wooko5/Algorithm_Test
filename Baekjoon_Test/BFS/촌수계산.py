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

def BFS(graph, node, target):
    global count # 전역변수를 지역변수로도 사용할 수 있게 선언
    need_visit = [node] # need_visit은 큐로 만들기 위함
    visited[node] = 1 # 방문했으니 1로 표시
    
    while need_visit: # need_visit에 더이상 방문할 노드가 없을 때까지 반복
        count += 1  # 방문했다면 일단 +1

        for _ in range(len(need_visit)): # need_visit의 길이만큼 반복
            node = need_visit.pop(0) # FIFO
            if node == target: # target 노드를 찾은 경우 count-1을 반환하고 끝내기
                return count - 1
            
            for i in graph[node]: # 아직 target 노드를 못 찾은 경우
                if visited[i] == 0: # 방문하지 않은 노드가 있다면
                    visited[i] = 1 # 방문처리하고 
                    need_visit.append(i) # need_visit에 추가
    return -1 # need_visit을 다 돌았는데 target 노드가 없다는건 이어지지 않았다는 것
print(BFS(family, A, B))