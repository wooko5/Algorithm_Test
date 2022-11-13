# 순열로 경우 수를 뽑아놓고 합이 0이 되는 경우만 카운트하기
from itertools import combinations

def solution(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer