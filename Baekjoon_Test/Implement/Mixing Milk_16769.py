capacity, milk = list(), list()

for _ in range(3):
    a, b = map(int, input().split())
    capacity.append(a); milk.append(b)

for i in range(100):
    index = i % 3 # 현재 우유 양동이를 가리키는 index
    next = (index+1) % 3 # 다음 우유양동이를 가리키는 next
    
    if milk[index] + milk[next] <= capacity[next]: # 현재 양동이와 다음 양동이 우유량을 합쳐도 다음 양동이 최대값보다 작거나 같은 경우
        milk[next] = milk[index] + milk[next]
        milk[index] = 0
    else: # 현재 양동이와 다음 양동이 우유량을 합쳐도 다음 양동이 최대값보다 큰 경우
        milk[index] = milk[index] + milk[next] - capacity[next] # 2, 0, 12 같은 경우
        milk[next] = capacity[next]
for i in milk:
    print(i)