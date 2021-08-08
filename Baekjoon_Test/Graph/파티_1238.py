import heapq, sys; input = sys.stdin.readline # https://bbbyung2.tistory.com/62, https://dojinkimm.github.io/problem_solving/2019/12/10/boj-1238-party.html
# 다익스트라 알고리즘을 제대로 알지 못하고 있었다
# 두번 다익스트라 하는 것을 알지 못 했다
# 나중에 다시 풀어보는 것을 권장한다
def dijkstra(start):
    queue = []
    distance = [INF] * (node + 1)
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node] < current_distance:
            continue

        for next_node, cost_node in graph[current_node]:
            cost = current_distance + cost_node # 현재 가중치 + 현재 노드까지의 가중치

            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
    return distance


# x로 가는 경우에는 node마다 다익스트라 알고리즘을 수행하여 각각의 가중치를 구하면 된다.
# 돌아오는 경우에는 x를 기준으로 다익스트라 알고리즘을 수행하면 된다.

INF = int(1e9)
node, edge, x = map(int, input().split())
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost)) # (도착지, 거리)

result = 0 
for i in range(1, node + 1):
    go = dijkstra(i) # i까지 가는 거리 
    back = dijkstra(x) # x까지 가는 거리
    result = max(result, go[x] + back[i]) # 집(i)에서 x까지 갔다가 집으로 다시 돌아오는 거리 중 최대값
print(result)