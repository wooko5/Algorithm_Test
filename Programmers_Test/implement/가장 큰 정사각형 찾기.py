"""
백준에서 똑같은 문제를 풀고 다시 푸는데도 생각은 났지만
구현에 실패함 역시 dp 문제에 잼병이다 다시 한번 풀어보자
2021.07.14
"""

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n):
        for index, j in enumerate(board[i]):
            matrix[i+1][index+1] = j # 원래 행+1, 열+1된 이중배열 생성

    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i][j]:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                answer = max(dp[i][j], answer)
    return answer**2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))