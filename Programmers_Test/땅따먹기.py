"""
정확성은 100%지만 너무 느려서 효율성에서 빵점인 코드
from copy import deepcopy
def solution(land):
    for i in range(1, len(land)):
        temp = deepcopy(land)
        first = max(land[i-1])
        idx = land[i-1].index(first)
        temp[i-1].pop(idx)
        for j in range(len(land[i])):
            if j != idx:
                land[i][j] += first
            else:
                land[i][j] += max(temp[i-1])
    return max(land[len(land)-1])

생각해보니 column의 개수가 4개 뿐이라 열이 겹치지않는 지난 행의 원소중에 가장 큰 max값을 다음 배열원소에게 
갱신시키면 마지막 행에 가장 큰 값을 알 수 있다
처음에 했던 방식으로 하면 [[1,2,3,4], [1,2,3,100], [5,6,7,8]] 인 경우, 
100을 거치지 않을 수 있기에 아래와 위 같은 방식으로 짰다
2021.07.07
"""

def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[-1])
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))