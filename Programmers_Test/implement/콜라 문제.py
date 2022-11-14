def solution(a, b, n):
    answer = 0
    share = 1
    # 총 n개의 콜라가 a미만인 경우 반복문을 빠져나옴
    while n >= a:
        share = n // a
        answer += share * b
        n = n - (share * a) + (share * b)
    return answer