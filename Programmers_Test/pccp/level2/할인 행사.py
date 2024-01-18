import collections


def solution(want, number, discount):
    answer = 0
    fruit = dict()

    for i in range(len(want)):
        fruit[want[i]] = number[i]

    for i in range(len(discount) - 9):
        limited_discount = discount[i : i + 10]

        if fruit == collections.Counter(limited_discount):
            answer += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
# result = 3
print(solution(want, number, discount))