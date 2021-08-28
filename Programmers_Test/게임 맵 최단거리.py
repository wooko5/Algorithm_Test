"""
하다가 말았다 계속해서 할 수 있도록!!!
처음에는 dfs로 풀었는데 bfs를 이용해서 푸는게 좋을 것 같다!
bfs로 처음 풀때는 28.6점이 나왔고, 
최소거리 이용하니깐 32.3점
(아마 그리디 버젼이라서 지금당장 가까운 거리로 간다해도 최종적으로는 돌아가는 방법이여서 틀린듯)
최종적으로 인터넷을 참조했다!!, visited[]를 False가 아닌 -1로 가득채운 그래프를 새로 만들어야 했다, 
세상에는 어마무시한 풀이법이 존재하는 것 같다 힘내자 ㅍㅇㅌ!!
2021.07.28
"""
def bfs(x, y, maps, visited):
    direcions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited[x][y] = 1
    queue = [[x, y]]

    while queue:
        x, y = queue.pop(0) # deque()의 popleft() 말고도 이렇게 가능
        
        for dx, dy in direcions:
            current_x, current_y = dx + x, dy + y
            
            if (0 <= current_x < len(maps)) and (0 <= current_y < len(maps[0])):
                if visited[current_x][current_y] == -1 and maps[current_x][current_y] == 1:
                    visited[current_x][current_y] = visited[x][y] + 1
                    queue.append([current_x, current_y])
    return visited[-1][-1] # 접근이 불가능 하다면 -1 반환이고, 가능하다면 지금까지 지나온 블록 반환

def solution(maps):
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    return bfs(0, 0, maps, visited) # 항상 (0, 0)에서 시작한다고 전제로 나와있음

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
#maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))