# BFS를 이용해야하지만 어떻게 이용할지 감조차 잡지 못했다 
# 다음에 다시 풀어봐야겠다
from collections import deque
def BFS():
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        z = d - x - y
        if x == y and y == z:
            print(1)
            return
        for i, j in (x, y), (x, z), (y, z):
            if i < j:
                j -= i
                i += i # i *= 2는 되지 않는다 -> visited[small][big]에서 index out of range 발생!!! 
            elif i > j:
                i -= j
                j += j # 아무래도 음수*음수는 양수가 되기 때문이지 않을까 싶다
            else:
                continue
            c = d - i - j
            small = min(i, j, c)
            big = max(i, j, c)
            if not visited[small][big]:
                queue.append((small, big))
                visited[small][big] = True
    print(0)

a, b, c = map(int, input().split())
d = a + b + c
visited = [[False]*d for _ in range(d)]
if d % 3:
    print(0)
    SystemExit(0)
else:
    BFS()