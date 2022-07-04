graph = dict()
graph[1] = [2, 5]
graph[2] = [1, 3, 5]
graph[3] = [2]
graph[4] = [7]
graph[5] = [1,2,6]
graph[6] = [5]
graph[7] = [4]

def DFS(graph, start):
    visited, need_visit = list(), list()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return len(visited)-1

print(DFS(graph,1))