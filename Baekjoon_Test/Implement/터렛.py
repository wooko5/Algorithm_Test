test_case = int(input())
for _ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    array = [distance, r1, r2]
    if distance == 0 and r1 == r2: # 두 원이 일치하는 경우 == 무한대
        print(-1)
    elif distance == r1 + r2 or max(array) == sum(array) - max(array): # 두 원이 한 점에서 만나는 경우 == 외접, 내접
        print(1)
    elif max(array) > sum(array) - max(array): # 두 원이 만나지 않는경우 == r,r1,r2중에 가장 큰 값이 나머지 합보다 큰 경우
        print(0)
    else: # 두 원이 두 점에서 만나는 경우 == 위의 3개를 제외한 나머지 전부
        print(2)