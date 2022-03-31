# 이 문제는 딕셔너리를 이용한다
"""
GCF + ACDEB가 최대가 되기 위해서는 자리수가 높은 A, C, G, D 이런순으로 높은 숫자를 가지면 된다.
이를 일반화 하기 위해서
A는 만의자리 수 이기 때문에 10000 값을 주고
C는 천의자리 수와 십의자리 수를 둘 다 가지기 때문에 1010 값을 준다.
G는 백의자리 수를 가지기 때문에 100
D는 백의자리 수를 가지기 때문에 100
E는 십의자리 수를 가지기 때문에 10
B는 일의자리 수를 가지기 때문에 1
F도 일의자리 수를 가지기 때문에 1을 준다.
이렇게 정렬을 해놓고 값이 높은 알파벳 순서대로 9부터 숫자를 준다.

A = 10000 * 9 = 90000
C = 1010 * 8 = 8080
G = 100 * 7 = 700
D = 100 * 6 = 600
E = 10 * 5 = 50
B = 1 * 4 = 4
F = 1 * 3 = 3
이를 다 더해주면 99437이라는 값이 나오게 되는 원리이다.
"""
answer = 0
array = []
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alphabet_list = []
for _ in range(int(input())):
    array.append(input())

for i in range(len(array)):
    for j in range(len(array[i])):
        alphabet_dict[array[i][j]] += 10**(len(array[i])-1-j)

for i in alphabet_dict.values():
    if i != 0:
        alphabet_list.append(i)
alphabet_list.sort(reverse=True)

for i in range(len(alphabet_list)):
    answer += alphabet_list[i]*(9-i)
print(answer)