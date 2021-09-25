# Heap, dataStructure, Greedy를 이용해서 푸는 문제
import heapq
test_csae = int(input())
array = []
answer = 0
for _ in range(test_csae):
    number = int(input())
    heapq.heappush(array, number)

while len(array) != 1: # 힙에 원소가 한 개만 남을 때까지 무한반복
    temp1 = heapq.heappop(array)
    temp2 = heapq.heappop(array)
    sum = temp1 + temp2 # 가장 최소 2개를 합치고 
    answer += sum # 정답에 더하고
    heapq.heappush(array, sum) # sum은 다시 heap에 넣기

print(answer)