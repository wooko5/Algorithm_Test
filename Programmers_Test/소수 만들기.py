from itertools import combinations
import math
def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def solution(nums):
    temp = []
    array = []
    answer = 0

    for i in nums:
        temp.append(str(i))
    
    com = list(combinations(temp, 3))
    
    for i in range(len(com)):
        array.append(list(map(int, com[i])))
    
    for i in range(len(array)):
        if isPrime(sum(array[i])):
            answer += 1
    
    return answer


nums = [1,2,3,4]
#nums = [1,2,7,6,4]
print(solution(nums))