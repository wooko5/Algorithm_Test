"""
큐나 스택문제인줄 알았지만 사실은 투포인터를 이용한 문제였다
잘못된 접근으로 인해 시간을 낭비하고, 결국 풀지 못 한채 다른 사람들의 코드를 힌트삼아서
겨우 통과할 수 있었다. 적어진 알고리즘 문제풀이 시간을 더 많이 쓸 수 있도록 노력해야겠다.
2021.09.16
"""

def solution(enter, leave):
    answer = [0] * len(enter)
    room = []
    enterIdx = 0

    for leavingPerson in leave:
        while leavingPerson not in room:
            room.append(enter[enterIdx])
            enterIdx += 1
        
        room.remove(leavingPerson)
        for roomPerson in room:
            answer[roomPerson - 1] += 1
        answer[leavingPerson - 1] += len(room)

    return answer

enter = [1, 4, 2, 3]
leave = [2, 1, 3, 4]
print(solution(enter, leave))