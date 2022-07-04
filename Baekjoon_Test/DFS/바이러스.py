computer = int(input())
network = int(input())
matrix = [[] for i in range(computer+1)] # 이중배열을 이런식으로도 만들 수 있다

for i in range(network):
    A, B = map(int, input().split())
    matrix[A].append(B) # 컴퓨터 A의 네트워크에 컴퓨터 B를 추가하기
    matrix[B].append(A) # 컴퓨터 B의 네트워크에 컴퓨터 A를 추가하기
                        # 네트워크가 양방향이라서 이렇게 해준다
def DFS(graph, start):
    visited, need_visit = list(), list()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return len(visited)-1
print(matrix[5])
print(DFS(matrix, 1))