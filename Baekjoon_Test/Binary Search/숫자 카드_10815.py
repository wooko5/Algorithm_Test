N = int(input())
sangGeun = list(map(int, input().split()))
M = int(input())
array = list(map(int, input().split()))
sangGeun.sort()
result = []

def binary_search(search): # 처음에 array(정수 집합)을 가지고 이진탐색했는데 생각해보니 상근이카드를 이진탐색해야함
    start = 0
    end = len(sangGeun)-1
    
    while start <= end:
        middle = (start+end)//2
        if search < sangGeun[middle]:
            end = middle - 1
        elif search > sangGeun[middle]:
            start = middle + 1
        else:
            return True #search가 sangGeun[middle]과 같다. True 반환
    return False #search를 sangGeun에서 아무리 찾아봐도 없다. False 반환

for i in array:
    if binary_search(i):
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i, end=' ')