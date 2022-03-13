n, l, k = map(int, input().split())
array = [] # 각 문제마다 현정이가 풀 수 있는 난이도 점수들의 집합 == 존재 x or 140 or 100 만 존재
result = 0
for _ in range(n): 
    sub1, sub2 = map(int, input().split()) # 쉬운 문제와 어려운 문제의 난이도를 입력받기
    if sub2 <= l: # 어려운 문제의 난이도가 현정이의 역량보다 같거나 작다면 
        array.append(140)
        continue # 어려운 문제를 풀었다면 굳이 쉬운 문제를 풀 필요가 없음
    elif sub1 <= l:
        array.append(100)

array.sort(reverse=True) # 내림차순 순으로 정렬(문제를 k개 뽑기위함)
if k < len(array): # 풀 수 있는 문제(len(array))보다 현정이가 시간 안에 풀 수 있는 문제의 수(k)가 적을 때
    for i in range(k):       
        result += array[i]
    print(result)
else: 
    print(sum(array))