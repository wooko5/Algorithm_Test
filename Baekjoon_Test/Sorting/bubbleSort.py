import random

def bubbleSort(num):
    for index in range(len(num)-1):
        swap = False
        for index2 in range(len(num)-index-1):
            if num[index2] > num[index2 + 1]:
                num[index2], num[index2 + 1] = num[index2 + 1], num[index2]
                swap = True
            
        if swap == False:
            break
        
        count += 1
    return num

#data_list = random.sample(range(100), 5)
data_list = [30, 10, 44, 27, 49]

print(data_list)
print("\n==============================================================\n")
count = 0
bubbleSort(data_list)
print(count)