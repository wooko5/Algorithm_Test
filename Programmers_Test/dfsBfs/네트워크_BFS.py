"""
기존의 인접행렬(0과 1로 구성된 이중배열)에서의 BFS는 알았지만 
네트워크를 모두 순회하는 방법은 몰랐다. 나중에 다시 한번 찾아보도록
힌트를 참조해서 풀었다
링크: https://cocojelly.github.io/algorithm/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-DFS-BFS-(2)/
2021.07.02
"""

def solution(n, computers):
    answer = 0
    visited = [0]*n
    queue = []

    while 0 in visited: 
    # 기존의 인접행렬 BFS를 하면 하나의 네트워크만 순회하므로 이렇게 하면 모든 네트워크를 순회한다
        queue.append(visited.index(0))
        visited[visited.index(0)] = 1
            
        while queue: # 전형적인 BFS 방식 순회
            node = queue.pop(0)
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    queue.append(i)
                    visited[i] = 1
        
        answer += 1 # 네트워크 하나의 순회가 끝났으면 answer + 1 해준다
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))