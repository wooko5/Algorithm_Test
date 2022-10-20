"""
이중반복문인줄 알고 고생하다가 힌트를 참조해서 풀었다
다음에 다시한번 풀어봐야겠다
2021.07.06
"""

def solution(A, B):
    answer = []
    for i in range(len(A)): # A의 행 길이(row)
        temp = []
        for j1 in range(len(B[0])): # B의 열 길이(column) 
            n = 0
            for j2 in range(len(A[0])): # A의 열 길이(column)
                n += A[i][j2] * B[j2][j1]
            temp.append(n)
        answer.append(temp)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]	
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))