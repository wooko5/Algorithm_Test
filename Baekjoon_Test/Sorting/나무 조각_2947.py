array = list(map(int, input().split()))
answer = sorted(array)
while answer != array:
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            print(*array)