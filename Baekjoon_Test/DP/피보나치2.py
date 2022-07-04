n = int(input())

#피보나치 dp 방법
def fibo_dp(num):
    #num을 저장할 리스트를 만든다
    cache = [ 0 for index in range(num+1)] #0으로 구성된 num길이만큼의 리스트생성
    cache[0] = 0
    cache[1] = 1
    
    for index in range(2, num+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[num]

print(fibo_dp(n))