K, N = map(int, input().split())
wire = []

for i in range(K):
    wire.append(int(input()))

result = 0 
low = 1
high = max(wire)

def check(number):
    count = 0
    for i in range(K):
        count += int(wire[i]/number)
    if count >= N:
        return True
    return False

while low <= high: # 이진탐색 수행
    middle = (low + high)//2
    if check(middle): # 조건에 만족하는 middle이라면
        if middle > result: # middle이 result보다 크다면
            result = middle # result는 middle이 된다
        low = middle + 1 # 탐색길이를 반으로 줄이고 이진탐색1
    else:
        high = middle - 1 # 탐색길이를 반으로 줄이고 이진탐색2
print(result)