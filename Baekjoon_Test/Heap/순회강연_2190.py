import heapq; array = []
for _ in range(int(input())):
    array.append(list(map(int, input().split()))) # [(paid, day)]로 array에 삽입
# array = sorted(array, key = lambda x: x[0]) # [(paid, day)]인데 paid를 오름차순으로 한 배열
array.sort(key=lambda x : x[1]) # [(paid, day)]인데 day를 오름차순으로 한 배열
print(array)
queue = []
for i in array:
    heapq.heappush(queue, i[0]) # paid를 queue에 우선순위식으로 push함
    print(queue)
    if (len(queue) > i[1]): # queue의 길이보다 day가 작다면 == 같은 day의 paid가 두 개 동시 존재한다면
        heapq.heappop(queue) # queue의 가장 작은 원소(paid)를 pop함
print(sum(queue))