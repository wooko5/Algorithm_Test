N,S = input(), input()   #OX문자열의 길이 N, OX문자열 S

#보너스 점수 bouns와 정규점수 score를 구분해서 써야할듯 
score, bonus =  0, 0

for index, OX in enumerate(S):  #index는 난이도이자 OX의 인덱스, OX
    if OX == 'O':
        score += 1 + index + bonus  #맞추면 정규점수+1+(점점상승하는)난이도+보너스점수
        bonus += 1                  #맞추면 보너스 점수+1
    else: 
        bonus = 0                   #못 맞추면 보너스 점수 초기화

print(score)