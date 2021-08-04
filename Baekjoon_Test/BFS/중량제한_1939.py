# 코딩대회에 나올 정도로 굉장히 어려운 문제
# M(다리개수, 엣지)는 10만이고, C(중량 제한)는 10억이다 매우 매우 큰 숫자
# O(M*logC)가 시간복잡도
# 즉 이진탐색을 통해 C(중량 제한)을 찾아야함
# BFS를 이용하고, 
def BFS(c):
    need_visit = [start_node] # 방문예정인 노드 저장
    visited = [0]*(N+1)
    visited[start_node] = 1 # 이미 방문한 노드를 1로 저장 
    while need_visit:
        x = need_visit.pop(0)
        for index, weight in matrix[x]:
            if visited[index] == 0 and weight >= c:
                visited[index] = 1
                need_visit.append(index)
    return visited[end_node]

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
start = 1000000000 # 10억
end = 1

for _ in range(M):
    A, B, weight = map(int, input().split())
    matrix[A].append((B,weight))
    matrix[B].append((A,weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())
answer = start

while start <= end:
    mid = (start+end)//2 # mid는 현재 중량을 의미
    if BFS(mid): # 중량을 만족하므로 섬간의 이동이 가능하므로 중량 증가
        answer = mid
        start = mid + 1
    else: # 섬간의 이동이 불가능하므로 중량 감소
        end = mid - 1

print(answer)