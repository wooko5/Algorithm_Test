
from copy import deepcopy


def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        arr = deepcopy(array)
        arr = arr[commands[idx][0]-1:commands[idx][1]]
        arr.sort()
        answer.append(arr[commands[idx][2]-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


# 2022.10.07 다시 품
def solution(array, commands):
    answer = []
    for start, end, index in commands:
        temp = array[start-1: end]
        temp.sort()
        answer.append(temp[index-1])
    return answer
