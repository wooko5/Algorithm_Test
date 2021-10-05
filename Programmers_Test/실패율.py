"""
각 스테이지마다 도달한 총 사용자의 수를 total_cnt로 구하고, 
스테이지에 도달했지만 아직 해당 스테이지를 해결 못 한 사용자 수를 fail_cnt로 구하고,
실패율을 구해서 answer에 [스테이지 번호, 실패율]을 삽입해서
람다식으로 1순위 실패율을 내림차순 정렬, 2순위 스테이지 번호 오름차순 정렬한다
정렬한 배열을 result에 넣고 반환하면 끝! 
ZeroDivisionError을 유의하면 쉽게 풀 수 있었던 문제였다. 5분 만에 풀고 제출하니깐 70점이 나오고 
런타임 오류가 나서 무슨 문제일까 고민하던 중에 문제에 '도달한 사람이 아무도 없는 스테이지의 실패율은 0'이라는 문장을 보고 수정할 수 있었다.
앞으로도 계속 문제를 꼼꼼히 읽는 습관을 들이자!
2021.10.05
"""

def solution(N, stages):
    answer = []
    result = []

    for i in range(1, N+1):
        total_cnt = 0
        fail_cnt = 0

        for j in stages:
            if j >= i:
                total_cnt += 1
                if j == i:
                    fail_cnt += 1
        if total_cnt == 0: # 도달하지 못 한 스테이지는 실패율을 0으로 해야한다
            answer.append([i, 0]) # 0으로 해놓지 않으면 실패율의 분모가 0으로 되는 ZeroDivisionError 발생
        else:
            answer.append([i, fail_cnt/total_cnt])

    answer = sorted(answer, key = lambda x : (-x[1], x[0]))

    for ans in answer:
        result.append(ans[0])
    return result