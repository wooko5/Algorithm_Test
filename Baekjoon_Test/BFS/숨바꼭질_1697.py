from collections import deque
N, K = map(int, input().split()) # N은 수빈의 위치, K는 동생의 위치
MAX = 100000+1
matrix = [0]*MAX

def BFS(graph, start, target):
    queue = deque([start])
    while queue:
        now_position = queue.popleft() # bfs 방식이므로 FIFO
        if now_position == target: # 만약 우리가 찾는 동생위치랑 현재 위치가 같다면
            return graph[now_position] # matrix값을 반환하고 루프문 나오기
        
        for next_position in (now_position-1, now_position+1, now_position*2): # 걷거나(-1, +1) 순간이동(*2)
            if 0 <= next_position < MAX and not graph[next_position]: # 다음 방문할 위치값이 최대값(N)보다 작고, 방문한 적이 없다면
                graph[next_position] = graph[now_position] + 1 # 다음 방문할 위치값은 현재 위치값+1을 해준다
                queue.append(next_position) # 앞으로 방문할 위치들을 큐에 넣어주기
print(BFS(matrix, N, K))