"""
9월의 마지막 풀이이자 위클리챌린지 8주차 문제 Level1정도로 매우 쉬웠다
가로와 세로 길이 모두에서 가장 큰 값을 bigNumber1이라는 변수로 생성하고,
또 다시 가로와 세로 길이를 반복문으로 처리하면서 둘 중 더 작은 값을 bigNumber2에 넣으면서 
가장 큰 값을 찾으려고 했다. 
이렇게 한 이유는 bigNumber1에 의해서 가로와 세로 중에 큰 값을 모두 처리가 되는데 사각형을 돌리면서 생기는
최솟값을 찾기 위해 bigNumber2을 이용했다
2021.09.30
"""

def solution(sizes):
    bigNumber1 = 0
    for width, height in sizes:
        if bigNumber1 < max(width, height):
            bigNumber1 = max(width, height)
    
    bigNumber2 = 0
    for width, height in sizes:
        if bigNumber2 < min(width, height):
            bigNumber2 = min(width, height)
    
    return bigNumber1 * bigNumber2