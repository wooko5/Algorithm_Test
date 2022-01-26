"""
저번처럼
이진트리 만드는데 O(NlogN), 후위순회하는데 O(NlogN)이라서 시간초과가 난다
트리를 만들지 않고 바로 출력하는 방식을 택해야한다

해결 방안:
첫번째 루트 노드를 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 나뉘는 것을 알 수 있다
ex) 50 / 30 24 5 28 45 / 98 52 60
이것을 이용해서 이진탐색의 원리로 범위를 수정해가면서 후위순회로 나올 올바른 index를 찾는다
"""
import sys; sys.setrecursionlimit(10**9)
def postOrder(start, end): # start = 0, end = 8
    if start > end:
        return
    
    division = end + 1
    for i in range(start+1, end+1):
        if array[start] < array[i]: # start(루트노드)가 비교 대상들 보다 더 작을 경우
            division = i
            break

    postOrder(start+1, division-1) # 왼쪽 
    postOrder(division, end) # 오른쪽
    print(array[start]) # 중앙

array = [] # 50 / 30, 24, 5, 28, 25 / 98, 52, 60ㄴ
count = 0
while count <= 10000: # 노드의 개수가 최대 10000개 이기 때문
    try:
        number = int(input()) # 50, 30, 24, 5 등등 
    except:
        break # 더 이상 전위순회한 노드가 없을 경우
    array.append(number) # 차례대로 배열에 넣기
    count += 1
postOrder(0, len(array)-1) # 배열의 index = 0부터 시작