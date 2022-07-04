"""
다시 풀어보자 당장 내일!!
2021.07.19
"""

import math
def solution(n, stations, w):
    answer = 0
    area = 2 * w + 1
    
    start = 1
    for s in stations:
        answer += max(math.ceil((s - w - start) / area), 0)
        start = s + w + 1
        
    if n >= start:
        answer += math.ceil((n - start + 1) / area)
    
    return answer

"""
def solution(n, stations, w):
    answer = 0
    idx = 0
    locate = 1

    while locate <= n:
        if idx < len(stations) and locate >= stations[idx] - w:
            locate = stations[idx] + w + 1
            idx += 1
        else:
            locate += 2*w+1
            answer += 1
    return answer
"""


n = 11
stations = [4, 11]
w = 1   

#n = 16	
#stations = [9]
#w = 2
print(solution(n, stations, w))