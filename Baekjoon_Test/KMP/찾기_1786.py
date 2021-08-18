def make_table(pattern):
    global matrix

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]: # j가 0이 되거나 i와 j 문자가 같을 때까지 반복
            j = matrix[j-1]

        if pattern[i] == pattern[j]: # i와 j 문자가 같다면 j를 증가
            j += 1
            matrix[i] = j # i번째 요소에는 인덱스 j를 저장

def KMP(sentence, pattern):
    global matrix

    j = 0
    for i in range(len(sentence)):
        while j > 0 and sentence[i] != pattern[j]:
            j = matrix[j-1]
        
        if sentence[i] == pattern[j]:
            if j == len(pattern)-1:
                answer.append(i - len(pattern) + 2) # 몇 번째 요소에서 찾았는지 알려줌
                j = matrix[j]
            else:
                j += 1

answer = []
sentence = input()
pattern = input()
matrix = [0]*len(sentence) # 기준이 될 큰 문자열로 matrix 생성
make_table(pattern) # 찾고싶은 부분문자열로 matrix 구성
KMP(sentence, pattern)
print(len(answer))
print(*answer)