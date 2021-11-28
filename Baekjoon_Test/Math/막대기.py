X = int(input())
data_list = [64,32,16,8,4,2,1]
count = 0 
for index in range(len(data_list)):
    if data_list[index] <= X:
        count += 1
        X -= data_list[index]

    if X == 0:
        break
print(count)