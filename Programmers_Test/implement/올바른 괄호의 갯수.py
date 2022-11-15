# Catalan number를 이용하는 문제, 전혀 몰랐음
def solution(n):
    denominator = 1
    numeratorA = 1
    numeratorB = 1
    for i in range(2 * n, 0, -1):
        denominator *= i
    
    for i in range(n, 0, -1):
        numeratorA *= i
        
    for i in range(n+1, 0, -1):
        numeratorB *= i
    
    return denominator/(numeratorA * numeratorB)