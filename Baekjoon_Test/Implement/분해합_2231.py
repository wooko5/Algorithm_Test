N = input() # '216'
answer = []
result = 0
for number in range(1, int(N)):
    temp = str(number)
    for i in range(len(temp)):
        result += int(temp[i])
    if int(temp) + result == int(N):
        answer.append(number)
    result = 0
if not answer:
    print(0)
else:
    print(min(answer))