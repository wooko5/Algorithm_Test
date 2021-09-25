import sys, heapq # 힙(최소값 이진트리)을 사용하지 않으면 시간초과가 나타난다 
input = sys.stdin.readline
test_case = int(input())
array = [] # 힙을 만들 리스트 생성
for _ in range(test_case):
    number = int(input()) # 0 또는 자연수를 입력받고
    if not array and number == 0: # 리스트에 아무 것도 없고, number가 0이라면 0을 출력하기
        print(0)
    elif array and number == 0: # 리스트에 원소가 존재하고, number가 0이라면 number를 추출(pop)하고 출력하기
        print(heapq.heappop(array))
    else: # number에 0을 제외한 양의 정수들이 왔을 때 
        heapq.heappush(array, number) # number가 자연수라면 리스트에 저장하기