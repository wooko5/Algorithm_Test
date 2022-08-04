"""
나 좀 이건 잘함, 한번에 풀었고, FIFO와 딕셔너리(Hash)의 원리를 이용했다
다른 사용자들의 풀이를 보니 나처럼 푼 방식은 거의 없고, Queue의 원리를 이용해서
선입선출하는 것 같다. 하하하 암튼 독창적이다고 생각함
2021.06.29
"""

import math
from collections import Counter

def solution(progresses, speeds):
    capacity = []
    array = []
    
    for p in progresses:
        capacity.append(100 - p)
    
    for i in range(len(capacity)):
        array.append(math.ceil(capacity[i]/speeds[i]))
        
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i+1] = array[i]
    
    return list(Counter(array).values())

progresses = [93, 30, 55]	
speeds = [1, 30, 5]
#progresses = [95, 90, 99, 99, 80, 99]	
#speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))