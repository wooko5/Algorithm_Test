"""
2월쯤 코딩테스트를 공부하기 시작할 때 이 문제를 프로그래머스에서 봤었다
그때는 못 풀었지만 지금은 파이썬으로 간단하게 풀 수 있었다. 
앞으로 자바를 이용해서 푸는 습관도 들일 생각이다 ㅍㅇㅌ!

1. 대부분 row의 관점에서 푸는 이중배열과는 다르게 column 관점에서 본다는 점이 다른 점이지만 딱히 어렵지 않았다.
2. 자신에게 준 점수를 pivot이라는 변수에 넣고, pivot을 제외한 해당 column의 점수 중에 최대값과 최소값을 temp_max/temp_min로 지정한다.
3. 해당 column에 대한 반복문이 끝나면 pivot이 temp_max보다 큰지, temp_min보다 작은지 판별한다.
4. pivot이 temp_max보다 크다는 의미는 유일한 최대값이기 때문에 합계인 num 계산 시 제외하고, chk = True로 바꾸고 check()함수를 호출한다. (temp_min도 동일)
5. chk가 True면 (column 길이 - 1)만큼으로 나누고, False면 column 길이로 합계 점수를 나눈다.
6. 구한 평균점수 number를 주어진 성적에 맞춰서 문자열을 반환한다.
2021.08.09
"""


def check(scores, number, chk):
    if chk:
        temp = number / (len(scores[0])-1)
    else:
        temp = number / len(scores[0])
    
    
    if temp >= 90:
        return 'A'
    elif (80 <= temp < 90):
        return 'B'
    elif (70 <= temp < 80):
        return 'C'
    elif (50 <= temp < 70):
        return 'D'
    else: 
        return 'F'
    

def solution(scores):
    answer =''
    
    for j in range(len(scores[0])):
        chk = False
        temp_max = -1
        temp_min = 101
        num = 0
        pivot = scores[j][j]
        
        for i in range(len(scores)):
            num += scores[i][j]
            if i != j:
                if scores[i][j] > temp_max:
                    temp_max = scores[i][j]
                if scores[i][j] < temp_min:
                    temp_min = scores[i][j]
        
        if pivot > temp_max or pivot < temp_min:
            num -= pivot
            chk = True
            
        answer += check(scores, num, chk)
    return answer
        