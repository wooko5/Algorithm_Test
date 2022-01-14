import math

def getPrime(number):
    is_prime = [False, False]+[True]*(number-1) # 처음 2개만 False 나머지는 True인 리스트 생성
    maximum = int(math.sqrt(number)) # number의 루트(제곱근) 구하기

    for index in range(2, maximum):
        if is_prime[index]:
            for j in range(2*index, number, index):
                is_prime[j] = False

    return [i for i in range(2, number) if is_prime[i]]

listPrimeNumbers = getPrime(100000)
setPrimeNumbers = set(listPrimeNumbers)

N = int(input())

for _ in range(N):
    num = int(input())
    answer = 0 
    while answer == 0:
        if not num in setPrimeNumbers:
            for prime in listPrimeNumbers:
                div = num//prime
                if num % prime == 0 and div in setPrimeNumbers and div != prime:
                    answer = num
                    break
        num += 1
    print(answer)