def solution(dartResult):
    answer = 0
    score = []
    number = ''
    for dart in dartResult:
        if dart.isdigit():
            number += dart
        else:
            if dart == 'S':
                number = int(number)**1
                score.append(number)
                number = ''
            elif dart == 'D':
                number = int(number)**2
                score.append(number)
                number = ''
            elif dart == 'T':
                number = int(number)**3
                score.append(number)
                number = ''
            elif dart == '*':  # 스타상(*) 당첨 시
                if len(score) >= 2:
                    score[-2] = score[-2]*2  # 바로 전에 얻은 점수와
                    score[-1] = score[-1]*2  # 해당 점수를 각 2배로 만든다
                else:
                    # 스타상(*)이 첫번째에 있는 경우, 해당 점수만 2배로 만든다
                    score[-1] = score[-1]*2
            elif dart == '#':  # 아차상(#) 당첨 시 해당 점수는 마이너스
                score[-1] = score[-1]*(-1)
    return sum(score)
