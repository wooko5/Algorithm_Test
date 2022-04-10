N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
answer = 0 

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        for q in range(j+1, len(arr)):
            sum = arr[i] + arr[j] + arr[q]
            if sum <= M:
                answer = max(answer, sum)
print(answer)
#정말 아까웠다 대신에 i+1, j+1 방식이 너무 좋았다 max(A,B), min(A,B)등 파이썬 라이브러리를 더 많이 써보자 