"""
문제 제목에서 알려주듯이 '정렬'에 관한 문제이고, 문제에서 주어지는 상황을 구현할 수만 있다면 쉽게 풀 수 있는 문제였다
[전체승률, 무거운 상대에게 이긴 횟수, 자신의 몸무게, 선수의 번호]를 boxerRecords라는 배열에 삽입해서
람다식을 통해 'key = lambda x : (-x[0], -x[1], -x[2], x[3])' 정렬에 성공했고, 
정렬된 boxerRecords의 boxerRecords[i][3]에 있는 선수 번호만 추출해서 answer에 삽입했다 
람다식을 이용한 다중 값 정렬을 통해 손쉽게 풀 수 있는 문제였지만 오랜만에 알고리즘을 푸는 상황으로 30분 정도 걸린 것 같다
2021.09.07
"""

def solution(weights, head2head):
    boxerRecords = []
    answer = []
    
    for i in range(len(head2head)): # weights 인덱스와 똑같음
        winning = 0
        losing = 0
        myWeight = weights[i]
        winningHeaviness = 0
        
        for j in range(len(head2head)):
            if head2head[i][j] == "W":
                winning += 1
                if weights[i] < weights[j]:
                    winningHeaviness += 1
                    
            elif head2head[i][j] == "L":
                losing += 1
                
        if winning == 0 and losing == 0:
            boxerRecords.append([0, winningHeaviness, myWeight, i+1])
        else:
            boxerRecords.append([winning/(winning+losing), winningHeaviness, myWeight, i+1])

    boxerRecords = sorted(boxerRecords, key = lambda x : (-x[0], -x[1], -x[2], x[3]))

    for boxer in boxerRecords:
        answer.append(boxer[3])
    return answer