import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # N은 나무의 개수, M은 집에 가져갈 나무 길이의 합
trees = list(map(int, input().split()))
left = answer = 0
right = max(trees)

while left <= right: # 전형적인 이진탐색 문제
    middle = (left+right)//2
    sum = 0
    for index in range(N):
        if middle < trees[index]: # (10 - 15) 경우 sum이 -5가 될 수 있으므로 거르기위함이다
            sum += trees[index] - middle
    if sum >= M: # 목표값보다 크거나 같다면
        answer = middle # 더 큰 값으로 바꿔치기 한다
        left = middle + 1
    else:
        right = middle - 1
print(answer)