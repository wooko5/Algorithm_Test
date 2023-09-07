'''
초기에는 for문을 두개 만들어서
1. 중복인 끝말잇기 찾기
2. 끝말잇기가 성립 안 하는 단어 찾기
했는데 테스트케이스 19, 20만 계속 틀려서
한번에 넣고 처리하는 방식을 고안해봤다.
'''
import math

def solution(n, words):
    answer = []
    array = [words[0]]
    
    for i in range(1, len(words)): # 1 ~ n-1
        array.append(words[i])
        j = i - 1 # before index
        
        if words[j][-1] != words[i][0] or array.count(words[i]) > 1: # 끝말잇기 잘못한 경우
            answer = get_position_and_turn(i, n) # 4, 2
            return answer
    
    if not answer:
        return [0,0]
    return answer


def get_position_and_turn(j, n):
    result = []
    position = n if (j + 1) % n == 0 else (j + 1) % n
    turn = math.ceil((j + 1) / n)
    result.append(position)
    result.append(turn)
    return result