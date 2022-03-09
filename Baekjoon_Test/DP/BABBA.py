#A, B는 피보나치 수열을 따른다. 갯수만을 세보자.
#그전에는 A, B를 다시 카운트해서 숫자로 변환하는 과정을 썼다 
#그러지말고 바로 숫자로 대입해서 피보나치로 풀면 바로 풀린다
K = int(input())
fibonacci = [0 for i in range(K+1)]
fibonacci[1] = 1

for i in range(2, K + 1):
    fibonacci[i] = fibonacci[i-1] +  fibonacci[i-2] 
print(fibonacci[K-1], fibonacci[K])