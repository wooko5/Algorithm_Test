import sys; input = sys.stdin.readline
n, m = map(int,input().split()) # n과 m이 각각 100만까지 가능이라 O(nm)은 파이썬으로 연산하기 힘듦
array = list(map(int, input().split())) # prefix_sum[4]는 4번째 array 원소까지의 합
prefix_sum = [0]*(n+1) # 그래서 누적합을 이용해서 풀어야합니다
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + array[i-1] # 이전 누적합과 현재 array원소를 합한 것을 현재 누적합에 넣기
for _ in range(m):
    i, j = map(int, input().split()) # i부터 j까지 합은 (i <= j)
    print(prefix_sum[j]-prefix_sum[i-1]) # j번째까지의 합에서 i-1번째까지 합을 빼면 가능