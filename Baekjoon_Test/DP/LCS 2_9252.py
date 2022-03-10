string_1 = list(input()) # ACAYKP
string_2 = list(input()) # CAPCAK

# dp를 이용한 matrix 생성
matrix = [[''] * (len(string_2) + 1) for _ in range(len(string_1) + 1)]
for i in range(1, len(string_1) + 1):
    for j in range(1, len(string_2) + 1):
        if string_1[i - 1] == string_2[j - 1]: # 두 문자열의 문자가 같은 경우
            matrix[i][j] = matrix[i - 1][j - 1] + string_1[i - 1]
        
        else: # 두 문자열의 문자가 같지 않은 경우
            if len(matrix[i - 1][j]) >= len(matrix[i][j - 1]):
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i][j - 1]

if len(matrix[-1][-1]) == 0: # LCS가 전혀 없을 때
    print(0)
else: # LCS가 존재할 때 
    print(len(matrix[-1][-1])) # LCS 길이
    print(matrix[-1][-1]) # LCS 출력