# 2021.05.05에 풀었음, 추후에 다시 풀어야겠다! 이해가 좀....
# 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. 
# (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
room_number = input() # 문자열로 받기
array = [0] * 10 # [0,0,0,0,0,0,0,0,0,0]

for i in room_number:
    if i == '6' or i == '9':
        if array[6] == array[9]:
            array[6] += 1
        else:
            array[9] += 1
    else:
        array[int(i)] += 1
    print(array)
print(max(array))