import sys
N, K = map(int, sys.stdin.readline().split())
array= list(map(int, sys.stdin.readline().split()))
array.sort()
print(array[K-1])
# 데이터의 개수가 최대 5000,000이다
# 시간 복잡도가 O(nlogn)의 정렬 알고리즘을 이용해야한다
# 예를 들면, 병합/퀵/힙 정렬, 혹은 파이썬의 기본 정렬 라이브러리 
# 시간적 이점을 위해 pypy3을 이용한다