'''
이중 for문이지만 hash라서 그런지, level1이라 그런지 시간제한에 걸리지 않았다(다행)
'''
def solution(name, yearning, photo):
    answer = []
    hash_map = dict()

    for i in range(len(name)):
        hash_map[name[i]] = yearning[i]

    for row in photo:
        result = 0
        for pht in row:
            if pht in hash_map:
                result += hash_map[pht]
        answer.append(result)

    return answer