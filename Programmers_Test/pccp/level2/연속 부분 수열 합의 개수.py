from copy import deepcopy

def solution(elements):
    answer = deepcopy(elements)
    start = 0 
    end = 0
    
    for i in range(1, len(elements)): # 길이 2~ elements의 전체 길이까지
        for j in range(len(elements)):
            start = j
            last = j + i + 1
            end = last if last <= len(elements) else last % len(elements)

            if start < end:
                answer.append(sum(elements[start:end]))
            else:
                temp = elements[start:]
                temp.extend(elements[:end])
                answer.append(sum(temp))
    return len(set(answer))

elements = [7,9,1,1,4]
print(solution(elements))