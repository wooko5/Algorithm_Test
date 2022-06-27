matrix = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    matrix.append((x, y)) # 람다를 이용해서 처음에는 y값 오름차순, y값이 같으면 x값 오름차순으로 정렬
matrix = sorted(matrix, key = lambda x : (x[1], x[0])) 
for x, y in matrix:
    print(x, y)