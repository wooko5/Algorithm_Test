n = int(input())
temp = n
count = 0
while True:
    if temp < 10:
        temp = temp*10 + temp
    else:
        temp = (temp % 10)*10 + ((temp//10 + temp % 10) % 10)
    count += 1
    if n == temp:
        break
print(count)