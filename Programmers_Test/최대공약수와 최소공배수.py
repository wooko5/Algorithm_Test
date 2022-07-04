"""
예전같았으면 math의 gcd, lcm 라이브러리 함수를 썼겠지만 
지금은 구현을 통해 통과했다 장하다!!
2021.07.15
"""

def gcd(n, m):
    for i in range(max(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i

def lcm(n, m):
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            return i

def solution(n, m):
    return [gcd(n,m), lcm(n,m)] # 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환