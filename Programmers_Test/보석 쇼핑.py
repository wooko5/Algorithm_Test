"""
처음에 set을 이용한 이중 for문으로 정확성은 맞았지만 효율성면에서는 최적화하기 힘들어서
답안을 보고 작성했습니다. 보고도 잘 이해가 가지 않아서 다시 풀어봐야겠습니다. 
프로그래머스 2020 카카오 인턴 문제, 레벨3
2021.11.15
"""

def solution(gems):
    answer = []
    gem_set = len(set(gems))  # 보석의 종류수
    gem_dictionary = {}  # 보석 종류별로 개수를 셀 딕셔너리

    start = 0  # 투 포인터의 시작점
    end = 0  # 끝점
    length = len(gems) + 1

    while end < len(gems):  # 끝점이 범위안에 있을 때만 검사

        if gems[end] not in gem_dictionary:  # 새로 발견한 보석
            gem_dictionary[gems[end]] = 1
        else:  # 기존에 존재하는 보석
            gem_dictionary[gems[end]] += 1

        end += 1  # 보석을 새로 추가했으니 end칸 한 칸 뒤로

        if len(gem_dictionary) == gem_set:  # 범위안에 모든 보석이 존재할 때
            while start < end:
                if gem_dictionary[gems[start]] > 1:  # 하나 이상 존재하면 뒤에도 더 존재한다는 뜻이므로
                    gem_dictionary[gems[start]] -= 1  # 하나를 제거해주고
                    start += 1  # start칸을 뒤로 한칸 이동
                elif end - start < length:  # 지정한 구간보다 현재 구간이 짧으면
                    length = end - start  # 지정한 구간 바꿔주기
                    answer = [start+1, end]
                    break
                else:
                    break

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))