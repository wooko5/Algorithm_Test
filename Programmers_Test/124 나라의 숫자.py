"""
dp 문제라 생각했지만 사실은 3진법에 관련된 내용이었다
당연히 못 풀었고 다음에 함 다시 봐야겠다
2021.06.30
"""

def solution(n):
    array = ['1','2','4']
    if n <= 3:
        return array[n-1]
    else: # 생략가능 
        q, r = divmod(n-1, 3) # q는 몫, r은 나머지, n-1이라는 숫자를 3으로 나눈 몫과 나머지
        return solution(q) + array[r]
n = 10
print(solution(n))