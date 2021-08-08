import heapq; import sys
INF = sys.maxsize
def dijkstra(graph, start):
    # 1)1~5번 노드에 INF를 배열에 넣는 코드
    dp = [INF]*(V+1)
    dp[start] = 0
    queue = []
    
    # 2)heapq.heappush(queue,[가중치, 시작 노드]) 처럼 거리배열
    heapq.heappush(queue, (0, start)) # 우선순위 큐라서 첫번째 매개변수에 가중치를 넣는다
    
    # 3)특정 노드와 거리를 가져오기
    while queue:
        current_distance, current_node = heapq.heappop(queue) # 가중치, 연결 노드
        
        # 이미 배열에 저장된 거리보다 현재 거리가 멀다면 그냥 업데이트를 스킵해주기 위해 나온것, 위의 6단계라 보면됨 
        if dp[current_node] < current_distance:
            continue
            
        # 4) 노드 이름와 거리(가중치)를 가져오기 
        for weight, next_node in graph[current_node]:
            distance =  weight + current_distance # 목표노드까지 거리 + 현재 노드까지 오는 거리
            
            if distance < dp[next_node]: # 만약에 현재 노드 거리가 기존의 distances배열에 저장된 거리보다 적다면  
                dp[next_node] = distance # 현재 노드의 거리로 바꿔주고  
                heapq.heappush(queue, (distance, next_node)) # 우선순위 큐에 추가함
    return dp

V, E = map(int, input().split()) # 정점 개수, 간선 개수
k = int(input()) # 시작 정점
matrix = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split()) # 5, 1, 1
    matrix[u].append((w,v)) # u번 노드 -> v번 노드의 가중치 w, 순서에 유의하자

answer = dijkstra(matrix, k)
for i in range(1, len(answer)):
    if answer[i] == INF:
        print('INF')
    else:
        print(answer[i])