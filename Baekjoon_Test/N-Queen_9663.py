N = int(input())
chess = [0]*(15+1)
result = 0
def check(x):
    for i in range(1, x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i:
            return False
    return True
    
def DFS(count):
    global result
    if count > N:
        result += 1
    else:
        for i in range(1, N + 1):
            chess[count] = i
            if check(count):
                DFS(count + 1)
DFS(1)
print(result)