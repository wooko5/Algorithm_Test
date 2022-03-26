N, Q = map(int, input().split())
time1 = list()
time2 = list()
time3 = list()
length = 0 

for i in range(N):
    time1.append(int(input()))

for j in range(Q):
    time2.append(int(input()))

for num in time1:
    length += num

for index in range(len(time1)):
    for i in range(time1[index]):
        time3.append(index+1)

for j in time2:
    print(time3[j])