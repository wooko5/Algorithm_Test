def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i]) # 해당 라인의 num[i]를 storage[i]로 수정
            clean_num.append(num[i])
            
    # 아래 코드에는 틀린 부분이 없습니다.
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer

storage = ["pencil", "pencil", "pencil", "book"]	
num = [2, 4, 3, 1]
# result = "pencil"

print(solution(storage, num))