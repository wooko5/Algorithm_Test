N = int(input())
array = [0]*1000001
array[1] = 1
array[2] = 2
for index in range(3, N+1):
    array[index] = (array[index-1] + array[index-2])%15746 # 출력문에 숫자를 붙여서 나누면 
    # int의 최대값을 벗어나기 때문에 처음부터 15746를 나누어준다 이게 핵심!!!
print(array[N])