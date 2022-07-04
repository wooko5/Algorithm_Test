target = input() # 목표 채널
buttons = int(input()) # 고장난 버튼의 개수
array = [i for i in range(10)] # 0 ~ 9까지의 버튼 배열
errors = list(map(int, input().split())) # 고장난 버튼들
for i in errors:
    array.remove(i)

result = ''
temp = 9
count = 0
number = 0
for i in range(len(target)):
    if int(target[i]) in array:
        result += target[i]
    else:
        for j in range(len(array)):
            if abs(int(target[i])-array[j]) < temp:
                temp = abs(int(target[i])-array[j])
                number = array[j]
        result += str(number)
        count += 1
if count == len(target):
    print(abs(int(target)-100))
    SystemExit(0)
else:
    print(abs(int(target) - int(result)) + len(target))