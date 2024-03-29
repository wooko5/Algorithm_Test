"""
첫 시도에는 4개 점을 2개씩 뽑는 조합으로 6가지 경우를 만들고
각각의 기울기를 구해서 array에 삽입해서 같은 기울기가 2개 이상 나오는지 확인했는데
굳이 그렇게 할 필요없이 아래 3가지의 기울기만 비교하면 됐다.
1) 1번째, 3번째 점의 기울기 와 2번째, 4번째 점의 기울기
2) 1번째, 4번째 점의 기울기 와 2번째, 3번째 점의 기울기
3) 1번째, 2번째 점의 기울기 와 3번째, 4번째 점의 기울기
"""


def solution(dots):
    x1, y1, x2, y2, x3, y3, x4, y4 = (
        dots[0][0],
        dots[0][1],
        dots[1][0],
        dots[1][1],
        dots[2][0],
        dots[2][1],
        dots[3][0],
        dots[3][1],
    )

    if ((y3 - y1) / (x3 - x1)) == ((y4 - y2) / (x4 - x2)):  # 1,3/2,4
        return 1
    if ((y2 - y1) / (x2 - x1)) == ((y4 - y3) / (x4 - x3)):  # 1,2/3,4
        return 1
    if ((y4 - y1) / (x4 - x1)) == ((y3 - y2) / (x3 - x2)):  # 1,4/2,3
        return 1
    return 0
