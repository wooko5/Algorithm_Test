n = int(input())
sangGeun = list(map(int, input().split(' ')))
sangGeun.sort()
m = int(input())
targets = list(map(int, input().split(' ')))
dic = dict()

for i in sangGeun:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if targets[i] in dic:
        print(dic[targets[i]], end=' ')
    else:
        print(0, end=' ')