from collections import Counter

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
counter = Counter(array)
counter = counter.most_common(2)
mode = counter[0][0]
if n > 1:
    if  counter[0][1] == counter[1][1]:
        mode = counter[1][0]
    
print(round(sum(array)/n)) # 산술평균, 소수점 첫번째자리에서 반올림
print(array[n//2]) # 중앙값
print(mode) # 최빈값
print(abs(array[-1] - array[0])) # 범위