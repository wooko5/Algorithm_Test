def solution(n):
    sum = 0
    for number in range(1, n+1):
        if n % number == 0:
            sum += number
    return sum