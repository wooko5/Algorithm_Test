def isPrime(number): # 이런 함수를 구현하면 시간복잡도가 O(sqrt(N)) 이다. 즉 N의 루트만큼이다 
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5)+1): #  2부터 i의 제곱근까지만 검사하면 
        if number % i == 0: # 나머지는 검사하나 마나여서 제곱근(루트)까지만 검사하면 되는 것이었다.
            return False
    return True

start, end = map(int, input().split())
for i in range(start, end+1):
    if isPrime(i):
        print(i)






def isPrime2(number): # 시간복잡도는 O(N)이므로 N의 크기가 크면 비효율적이다. 
    # 문제는 N이 100만까지 올라갈 수 있어서 이 함수는 시간초과뜸 == 오류!
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True