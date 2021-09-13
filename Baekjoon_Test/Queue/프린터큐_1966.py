import sys
input = sys.stdin.readline
test_case = int(input()) # 전체 테스트 케이스 개수
queue = []
for _ in range(test_case): 
    n, m = map(int, input().split())        #  0 1 2 3 -> index
    queue = list(map(int, input().split())) # [2,1,4,3] -> 원소
    queue = [(number, index) for index, number in enumerate(queue)] # [(1,1), (4,2), (3,3), (2,0)] queue
    count = 0                                                       # [(1,1), (2,0), (3,4), (4,2)]는 max(queue)
    while True:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]: # 현재 가장 중요도가 높은 문서가 queue 제일 앞에 있다면
            count += 1
            if queue[0][1] == m: # 만약에 queue의 맨 앞 문서가 우리가 원하는 m 문서라면
                print(count) # 횟수를 출력하고 끝내기
                break
            else: # 만약에 queue의 맨 앞 문서가 우리가 원하는 m 문서가 아니라면
                queue.pop(0) # queue의 맨 앞 문서를 빼기
        else: # 현재 가장 중요도가 높은 문서가 queue 제일 앞에 있는게 아니라면
            queue.append(queue.pop(0)) # 큐에 push하는건데, 큐의 가장 앞에 있는 놈을   
        # queue =  (1,1), (4,2), (3,3), (2,0), (중요도값, index)