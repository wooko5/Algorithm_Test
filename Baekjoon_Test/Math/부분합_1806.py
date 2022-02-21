n, s = map(int, input().split())
array = list(map(int, input().split()))
sumArray = [0]*(n+1) # 누적합 배열
for i in range(1, n+1):
    sumArray[i] = sumArray[i-1] + array[i-1]
start = 0
end = 1
answer = []
while start <= n-1 and end <= n:
    if sumArray[end] - sumArray[start] >= s:
        answer.append(end - start)
        start += 1
    
    else: # sumArray[end] - sumArray[start] < s:
        if end == len(sumArray)-1: # end가 sumArray의 마지막 index라면
            start += 1 
        else: # end가 sumArray의 마지막 index가 아니라면 
            end += 1
if answer:
    print(min(answer))
else:
    print(0)