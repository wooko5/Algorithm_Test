from itertools import permutations

"""
처음에 문제 접근법이 '순열'임을 몰라서 좀 헷갈렸지만
인터넷을 통해 문제 접근법을 알게 되었고, 동굴의 최대 개수가 8개 이므로 
방문 순서를 순열을 통해 모두 알아내도 효율성에 문제가 없을 것 같았습니다. 
2021.11.08
"""

def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : (-x[0], x[1]))
    pool = [str(i) for i in range(len(dungeons))]
    visited_order = list(permutations(pool))
    
    for order in visited_order:
        health = k
        count = 0
        
        for i in order:
            index = int(i)
            if dungeons[index][0] <= health:
                health -= dungeons[index][1]
                count += 1
        answer = max(answer, count)
    return answer