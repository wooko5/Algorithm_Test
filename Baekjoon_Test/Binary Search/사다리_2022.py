"""
이 문제는 이진탐색이지만 사실상 닮음비성질과 피타고라스정리를 알아야만 푸는
수학 문제가 아니었나 싶다. 특히 middle값을 어떻게 추정할지 몰랐다
다음에 다시 풀어보는게 좋을 것 같다
"""
import math; x, y, c = map(float, input().split())
start = 0 
end = min(x, y)
# 1e9 = 1*(10**9) = 1000000000, 2e9 = 2*(10**9) = 2000000000
while abs(end - start) > 1e-6: # 1e-6 = 1*(10**-6) = 0.000001 # 두 수의 차이가 0.000001보다 커야함
    middle = (start + end) / 2.0
    
    d = middle # 우리가 구해야할 답
    
    h1 = math.sqrt(x**2 - d**2)
    
    h2 = math.sqrt(y**2 - d**2)
    
    h = (h1 * h2) / (h1 + h2)
    
    #print('h는 %f'%h, 'c는 %f'%c, 'mid는 %f'%middle)
    
    if h > c: # h가 c보다 큰 것은 우리가 찾아야할 정답이 오른쪽에 치우쳐 있음을 의미
        start = middle
    
    else: # h가 c보다 작거나 같은 것은 우리가 찾아야할 정답이 왼쪽에 치우쳐 있음을 의미
        end = middle
print("%.3f" % round(middle, 3)) # 절대/상대 오차는 0.001 까지 허용