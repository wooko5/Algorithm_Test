def solution(k, tangerine):
    tangerine.sort()
    orange_dictionary = dict()
    value = 0

    for size in tangerine: # collections.Count(tangerine)를 통해서 같은 결과를 만들 수 있음
        if size in orange_dictionary:
            orange_dictionary[size] += 1
        else:
            orange_dictionary[size] = 1
    
    array = sorted(orange_dictionary.items(), key=lambda x : x[1], reverse=True) # [[key, value], ...] 

    for index in range(len(array)):
        value += array[index][1]
        if value >= k:
            return index + 1


k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
# result = 2

print(solution(k, tangerine))