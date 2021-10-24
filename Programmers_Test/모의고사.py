"""
아주 옛날에 풀었는데 기억 안 나서 다시 풀고, 맞춤 ㅎㅎㅎㅎㅎ
2021.06.29
"""

def solution(answers):
    scores, answer = [0, 0, 0], []
    player1 = [1, 2, 3, 4, 5]*2000
    player2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

    for i in range(len(answers)):
        if answers[i] == player1[i]:
            scores[0] += 1
        if answers[i] == player2[i]:
            scores[1] += 1
        if answers[i] == player3[i]:
            scores[2] += 1

    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i+1)
    
    return answer

answers = [1,2,3,4,5]
#answers = [1,3,2,4,2]
print(solution(answers))
