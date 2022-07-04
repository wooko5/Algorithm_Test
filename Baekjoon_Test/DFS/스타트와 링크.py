import sys
N = int(input())
visited = [False]*21 # N의 최대값이 20이므로 그것보다 +1 해준다
matrix = [] # S 배열을 담을 이중배열 생성
answer = sys.maxsize # 정수의 시스템 최대값

def DFS(current_player, count):
    global answer 
    if count == N/2:
        team_link = [] 
        team_start = []
        for i in range(N):
            if visited[i]:
                team_start.append(i)
            else:
                team_link.append(i)
        
        power_start, power_link = 0, 0
        for i in range(len(team_start)):
            for j in range(i+1, len(team_start)):
                start_x = team_start[i]
                start_y = team_start[j]
                link_x = team_link[i]
                link_y = team_link[j]
                power_start += matrix[start_x][start_y] + matrix[start_y][start_x]
                power_link += matrix[link_x][link_y] + matrix[link_y][link_x]
        answer = min(answer, abs(power_start - power_link))
        return
    
    for i in range(current_player+1, N):
        if visited[i] == False:
            visited[i] = True
            DFS(i, count+1)
            visited[i] = False

for _ in range(N):
    matrix.append(list(map(int, input().split())))

DFS(0, 0)
print(answer)