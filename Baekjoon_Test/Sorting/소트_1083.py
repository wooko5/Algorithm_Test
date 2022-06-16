# 버블소트를 이용한 것은 알았지만 
# n = 5, array = [1, 2, 3, 4, 5], m = 4일 때 
# 5 1 2 3 4로 나오는 것을 캐치하지 못함(테스트케이스) 불예측
# 구현화와 세밀함에 좀 더 집중해야겠다 
n = int(input()) # 7
array = list(map(int, input().split()))
count = int(input())

for i in range(n):
    if count <= 0:
        break
    max_number = array[i]
    max_index = i
    for j in range(i+1, n):
        if count - (j - i) >= 0:
            if max_number < array[j]:
                max_number = array[j]
                max_index = j
    
    for k in range(max_index, i, -1):
        array[k], array[k-1] = array[k-1], array[k]
    count -= max_index - i
for i in array:
    print(i, end=' ')