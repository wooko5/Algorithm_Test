def isPrime(n):
    array = [False, False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if array[i]: # 처음 받는 수는 넣고, 예를 들어 i가 2이면
            primes.append(i)
            for j in range(2*i, n+1, i): # 처음 수의 배수가 되는 숫자는 모두 false로 제거, 예를 들어 2의 배수들 모두 제거
                array[j] = False
    return primes # 소수들의 배열
 
number = int(input())
array = isPrime(4000000) # 2부터 400만까지의 소수를 모아둔 배열 
answer = 0
start = 0
end = 1

sumArray = [0]*(len(array)+1) # 누적합 배열
for i in range(1, len(array)+1):
    sumArray[i] = sumArray[i-1] + array[i-1]

while start <= end:
    if sumArray[end] - sumArray[start] > number:
        start += 1
    
    elif sumArray[end] - sumArray[start] == number:
        answer += 1
        start += 1
    
    else:
        if end == len(sumArray) - 1:
            start += 1
        else:
            end += 1
print(answer)