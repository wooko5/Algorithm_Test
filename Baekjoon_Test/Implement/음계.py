arr = list(map(int, input().split(' ')))
count = 0

for index in range(len(arr)-1):
    if arr[index+1] ==  arr[index]+1:
        count += 1
    elif arr[index+1] ==  arr[index]-1:
        count += -1
    else: 
        count *= 0
        break

if count > 0:
    print('ascending')
elif count < 0:
    print('descending')
else:
    print('mixed')

#1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed