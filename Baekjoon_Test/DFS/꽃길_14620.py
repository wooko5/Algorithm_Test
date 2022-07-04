n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)] # 가만히 있는 것도 포함
answer = 10000

def check(array): # 꽃이 a, b, c에 있을 때 비용
    result = 0
    flower = []
    for i in array:
        x = i // n # 나눈 값
        y = i % n # 나머지
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            return 10000
        
        for dx, dy in directions:
            current_x, current_y = x + dx, y + dy
            flower.append((current_x, current_y))
            result += matrix[current_x][current_y]
    
    if len(set(flower)) != 15: # 꽃잎 3개가 차지하는 크기가 15라서, 15가 안 된다면 3개를 못 기른다는 뜻임 
        return 10000
    return result

for i in range(n*n):
    for j in range(i+1, n*n):
        for k in range(j+1, n*n):
            answer = min(answer, check([i, j, k]))
print(answer)