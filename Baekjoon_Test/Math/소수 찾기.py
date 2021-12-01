def isPrime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

N = int(input())
array = list(map(int, input().split()))
count = 0
for i in array:
    if isPrime(i):
        count += 1
print(count)