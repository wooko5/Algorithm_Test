# 데이터의 개수가 10,000,000개라서 완전 많지만 데이터의 범위가 10,000까지 이므로 작다
# 이를 이용해서 '계수정렬'을 이용해서 풀어본다
# '계수정렬'은 배열의 index를 특정한 데이터 값으로 여기는 정렬 방법이다
# 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
# 데이터가 등장한 횟수를 셉니다
# 데이터의 개수가 많을 때는 sys.stdin.readline을 이용한다
import sys
input = sys.stdin.readline
N = int(input())
array = [0]*(10000+1) # 계수정렬을 위해 10000+1개의 리스트를 만든다

for _ in range(N):
    array[int(input())] += 1 # index에 맞는 숫자가 올 때마다 가중치 +1 해준다

for i in range(10000+1):
    if array[i] != 0: # 해당 요소에 index에 맞는 숫자가 삽입됐다면
        for j in range(array[i]): # 가중치만큼 출력
            print(i)