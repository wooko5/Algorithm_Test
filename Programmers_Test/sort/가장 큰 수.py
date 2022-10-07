"""
오랜만에 자바로 코딩테스트 문제를 풀다가 아무래도 문자열 관련은 파이썬이 효율적이기에 풀게 되었다
프로그래머스 레벨2의 상당히 쉬운 문제로 문자 정렬에 대해 알고있다면 쉽게 풀었을 것이다.
대신 'key = lambda x : x * 3'처럼 numbers의 원소가 1000 이하라서 x를 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻이다
2021.10.27
"""
def solution(numbers):
    numbers = sorted(list(map(str, numbers)),
                     key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


def solution(numbers):
    answer = ''
    number_set = {}
    array = []
    for i in range(len(numbers)):
        tmp = str(numbers[i]) + "000"
        number_set[i] = int(tmp[:4])

    for key, values in number_set.items():
        array.append([key, values])

    temp = sorted(array, key=lambda x: -x[1])

    for i in range(len(temp)):
        answer += str(numbers[temp[i][0]])
    return answer
