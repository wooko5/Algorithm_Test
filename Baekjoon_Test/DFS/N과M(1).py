# 조합의 개수를 구하는 문제이므로, dfs를 활용하여 풀이가 가능하다.
# 각 숫자는 순열에서 딱 한번만 사용되므로, 각 숫자를 인덱스로 가지는 bool형 배열인 visited를 선언하고,
# 해당 숫자를 뽑았는지 유무를 저장한다. 
# 숫자를 앞에서부터 한개씩 뽑아가면서 visited가 M개만큼 true가 되면, 출력을 해주는 재귀함수를 활용하면 된다.

N, M = map(int, input().split())
MAX = 8 + 1
arr, visited = list(), list()
arr = [0 for _ in range(MAX)]
visited = [0 for _ in range(MAX)]

def DFS(count):
    if count == M:
        for i in range(M):
            print(arr[i],end=" ")
        print("")
        return
    for i in range(1, N+1):
        if visited[i] == False: # 방문하지 않았다면
            visited[i] = True   # 방문한 걸로 고치고
            arr[count] = i      # 그 자리에 자연수를 넣고
            DFS(count+1)        # 다시 DPS 재귀호출
            visited[i] = False 
DFS(0)
