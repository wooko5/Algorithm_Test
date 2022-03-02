T = int(input()) # 테스트 케이스 숫자
n = []

def case(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return case(n-1)+case(n-2)+case(n-3)

for i in range(T):
    n.append(int(input()))

for number in n:
    print(case(number))