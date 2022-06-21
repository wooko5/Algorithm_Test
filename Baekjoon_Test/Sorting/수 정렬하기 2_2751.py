test_case = int(input())
array = []
for _ in range(test_case):
    x = int(input())
    array.append(x)
array.sort()
for i in array:
    print(i)