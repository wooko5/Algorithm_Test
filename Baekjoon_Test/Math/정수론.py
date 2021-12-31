# gcd란 greatest common divider = 최대공약수
# 방법 1: 단순하게 반복문 사용
def gcd_naive(a, b): 
    for i in range(min(a, b), 0, -1):
        if a%i == 0 and b%i == 0:
            return i

# 방법 2: 유클리드 호제법 사용(재귀함수)
def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

# 방법 3: 유클리드 호제법을 반복문으로 변경
def gcd2(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b

# 방법 4: math의 gcd 이용하기
import math
a, b = 10, 24
math.gcd(a, b)

print(gcd_naive(10, 24)) # 가장 느림
print(gcd(10, 24))
print(gcd2(10, 24)) 
print(math.gcd(10, 24)) # 가장 시간복접도가 빠름 -> 라이브러리는 c/c++로 최적화되어있기 때문


# 최소공배수 least common multiple
def lcm(a, b):
    return a*b/math.gcd(a,b)


# 에라토스테네스의 체 == 소수를 구하는 효율적인 알고리즘
def era_prime(N): # 2부터 N까지의 소수배열을 반환하는 함수
    A, p = [0 for _ in range(N+1)], []
    for i in range(2, N):
        if A[i] == 0:
            p.append(i)
        else:
            continue
        for j in range(i**2, N, i):
            A[j] = 1
    return p
print(era_prime(100))