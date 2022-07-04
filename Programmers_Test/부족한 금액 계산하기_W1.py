"""
오늘부터 프로그래머스에서 매주 1문제씩 나오는 챌린지가 생겼다.
어떤 문제들이 나올지 궁금한데 역시나 첫 문제는 단순 구현 문제가 나왔다
앞으로 초심잃지 말고 매주 그리고 매일 알고리즘 1문제 이상씩 풀 수 있도록 노력하자 ㅍㅇㅌ!
2021.08.03
"""
def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price*i
    if money - answer < 0:
        return abs(money - answer)
    return 0