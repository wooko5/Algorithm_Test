#이해가 안 가는 수학 실버1 문제 
#나중에 꼭 다시 보길! 
import math
T = int(input())
def counter(distance):
    count = 0 
    n = int(math.sqrt(float(distance)))
    count += 2 * n - 1
    distance -= math.pow(n , 2)
    count += distance/n
    distance %= n
    if distance>0:
        count += 1
    return int(count)

for _ in range(T):
    x, y = map(int, input().split())
    distance = y-x
    count = counter(distance)
    print(count)