def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            DFS(n, computers, i, visited)
            answer += 1 # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면, 네트워크 한개를 순회한 것
    return answer

def DFS(n, computers, node, visited):
    visited[node] = 1
    for i in range(n):
        if visited[i] == 0 and computers[node][i] == 1: # 현재 노드와 연결된 컴퓨터들을 DFS순회하라
            DFS(n, computers, i, visited)