"""
링크: https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-DFS-BFS-Python
2021.07.02
"""

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

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))