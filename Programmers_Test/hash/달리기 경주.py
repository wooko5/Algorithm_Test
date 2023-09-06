'''
처음에는 간단하게 파이썬식 swap(a, b = b, a)를 이용해서
array.index()를 통해 players 배열에서 바로 자리를 바꿨지만
시간초과!
그래서 해시(딕셔너리) 구조로 바꿔서 처리하니 통과
별거 아닌데 꽤나 고민을 많이 하게됐다...
'''
def solution(players, callings):
    answer = []
    hash_map = dict()
    for i in range(len(players)):
        hash_map[players[i]] = i + 1
    reversed_map = dict(map(reversed, hash_map.items()))
    
    for call in callings:
        source_rank = hash_map[call] # 4
        target_rank = hash_map[call] - 1 # 3
        old_player = reversed_map[target_rank] # poe
        new_player = reversed_map[source_rank] # kai
        reversed_map[target_rank], reversed_map[source_rank] = new_player, old_player
        hash_map[new_player], hash_map[old_player] = target_rank, source_rank
        
    for value in reversed_map.values():
        answer.append(value)
    return answer


players = ["mumu", "soe", "poe", "kai", "mine"]	
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))