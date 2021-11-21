#시간초과 뜸
import math
n = int(input())
x = list()
y = list()
answerForX = list()
answerForY = list()
answer = list()

for i in range(n):
    width, height = map(int, input().split())
    x.append(width)
    y.append(height)

for i in range(len(x)-1):
    for j in range(i+1, len(x)):
        answerForX.append(int(math.pow(x[j],2)-math.pow(x[i],2)))
        answerForY.append(int(math.pow(y[j],2)-math.pow(y[i],2)))

for index in range(len(answerForX)):
    answer.append(answerForX[index] + answerForY[index])

print(abs(min(answer)))