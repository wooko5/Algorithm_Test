n = int(input())
sangGeun = list(map(int, input().split(' ')))
sangGeun.sort()
m = int(input())
targets = list(map(int, input().split(' ')))

def down_binary(target): # 찾고자 하는 목표물이 중복일 경우 가장 왼쪽의 index를 반환하는 이진탐색 함수
    start = 0
    end = len(sangGeun) - 1

    while start <= end:
        mid = (start + end) // 2

        if sangGeun[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

def up_binary(target): # 찾고자 하는 목표물이 중복일 경우 목표물보다 큰 최초 원소의 index를 반환하는 이진탐색 함수
    start = 0
    end = len(sangGeun) - 1

    while start <= end:
        mid = (start + end) // 2
            
        if sangGeun[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(m):
    print(up_binary(targets[i]) - down_binary(targets[i]), end=' ')