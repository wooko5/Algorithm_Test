from itertools import combinations
import sys

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

player_list = [i for i in range(N)]
result = sys.maxsize

def solve():
    global result
    
    # 조합을 이용하여 각 후보자를 생성함
    for candidate in combinations(player_list, N // 2):
        # 선택된 후보와 나머지
        start_member = list(candidate)
        link_member = list(set(player_list) - set(candidate))
        
        # 점수 비교는 2명씩 이루어진다.
        start_comb = list(combinations(start_member, 2))
        link_comb = list(combinations(link_member, 2))
        
        # 점수 구하기
        start_sum = 0
        for x, y in start_comb:
            start_sum += (matrix[x][y] + matrix[y][x])
            
        link_sum = 0
        for x, y in link_comb:
            link_sum += (matrix[x][y] + matrix[y][x])
        
        # 차이를 구하는 것이므로 abs 사용
        if(result > abs(start_sum - link_sum)):
            result = abs(start_sum - link_sum)
            
solve()
print(result)