test_case = int(input()) # 콤비네이션 + 재귀함수로 풀었당
def pactorial(number):
    if number == 1:
        return number
    return number*pactorial(number-1)

for _ in range(test_case):
    west, east = map(int, input().split())
    if east - west == 0:
        print(1)
    else:
        print(int(pactorial(east)/(pactorial(east-west)*pactorial(west))))