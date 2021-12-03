S = int(input())
sum = 0 
i = 1

while True:
    sum += i
    if sum == S:
        break
    elif sum > S:
        i -= 1
        break
    i += 1

print(i)