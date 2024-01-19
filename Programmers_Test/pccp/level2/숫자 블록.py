import math

"""
6 => 1 2 3 6
결론: 해당 숫자를 제외한 최대공약수를 구하기
"""


def solution(begin, end):
    answer = []

    for number in range(begin, end + 1):
        if number == 1:
            answer.append(0)
        else:
            answer.append(greatest_common_divisor(number))
    return answer


def greatest_common_divisor(number):
    temp = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if number // i > 10000000: # 10000000를 넘는 경우를 생각하지 못 했음, 1 ≤ begin ≤ end ≤ 1,000,000,000
                temp.append(i)
            else:
                temp.append(number // i)
    return max(temp) if temp else 1


begin = 100000014
end = 100000016
# begin = 1
# end = 10
print(solution(begin, end))
