import sys; input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
k = -1; m = -1

for i in range(len(array)-1):
    if array[i] > array[i+1]:
        k = max(k, i) # a[k] > a[k+1]을 성립하는 최대값 k찾기

if k == -1: # 맨 처음 순열이라면 이전 순열이 없으므로 -1 출력
    print(-1)
else:
    for j in range(k+1, n): # k이후부터 배열 끝까지 인덱스 중에
        if array[k] > array[j]: # a[k] > a[m]이 성립하는 최대값 m찾기
            m = max(m, j)
    array[k], array[m] = array[m], array[k] # 두 인덱스에 해당하는 값을 서로 바꿔주고
    answer = array[:k+1]  
    answer += sorted(array[k+1:], reverse=True) # k인덱스 이후부터 내림차순으로 정렬하기
    print(*answer)