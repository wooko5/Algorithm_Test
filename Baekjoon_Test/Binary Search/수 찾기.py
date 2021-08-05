N = int(input())
data_list_A = list(map(int, input().split()))
data_list_A.sort()
M = int(input())
data_list_B = list(map(int, input().split()))

def binarySearch(data,search):
    start = 0
    end = len(data)-1

    while start <= end:
        medium = (start+end)//2
        if search == data[medium]:
            return 1
        elif search > data[medium]:
            start = medium + 1
        else:
            end = medium - 1
    return 0

for index in range(len(data_list_B)):
    print(binarySearch(data_list_A, data_list_B[index]))