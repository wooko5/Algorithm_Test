
"""
from itertools import permutations
def solution(n, k):
    answer = []
    array = [str(i) for i in range(1, n+1)]
    array = list(permutations(array, n))
    for i in array[k-1]:
        answer.append(int(i))
    return answer

"""

import math
def solution(n, k):
    answer = []
    array = [i for i in range(1, n+1)]
    
    while n != 0:
        number = math.factorial(n-1)
        index, k = (k-1)//number, k % number
        answer.append(array.pop(index))
        n -= 1
    return answer

n = 3
k = 5
print(solution(n, k))