"""
def solution(brown, yellow): # 테스트케이스 4,6,7이 계속 틀리는데 이유를 모르겠다 ㅂㄷㅂㄷ
    # 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
    total = brown + yellow
    answer = []
    for i in range(total, int(total**0.5)-1, -1):
        if total % i == 0:
            horizontal = i # 가로 
            vertical = total // i # 세로 
            answer.append((horizontal, vertical))
    
    if answer[-1][0] >= answer[-1][1]:
        return [answer[-1][0], answer[-1][1]]
    return [answer[-1][1], answer[-1][0]]

결국 근의 공식을 이용한 수학방식으로 풀었다, 추후에 다른 방식으로 풀어보는 거 강추
2021.07.12
"""

def solution(brown, yellow):
    x = int((brown + 4 + ((brown+4)**2 - 16*(brown + yellow))**0.5)/4)
    y = int((brown + yellow) // x)
    
    if x >= y: # 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
        return [x, y]
    return [y, x]

brown = 24
yellow = 24
print(solution(brown, yellow))