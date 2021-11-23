N = int(input())
F = int(input())
ten = N % 100 
hundred = N-ten
answer = list()
for i in range(0, 10):
    for j in range(0, 10):
        if (hundred+(i*10)+j) % F == 0:
            if i == 0:
                answer.append(j)
            answer.append(i*10+j)
            
arr = min(answer)
if arr/10 < 1:
    print("0"+str(arr))
else:
    print(arr) 