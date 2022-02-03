def make_table(pattern):
    matrix = [0]*len(pattern) # 기준이 될 큰 문자열로 matrix 생성
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]: # j가 0이 되거나 i와 j 문자가 같을 때까지 반복
            j = matrix[j-1]

        if pattern[i] == pattern[j]: # i와 j 문자가 같다면 j를 증가
            j += 1
            matrix[i] = j # i번째 요소에는 인덱스 j를 저장
    return max(matrix)

sentence = input()
answer = 0
for i in range(len(sentence)):
    answer = max(answer, make_table(sentence[i:]))
print(answer)