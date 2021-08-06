# 혼자서 짜서 맞은 문제인데 그 전에 짰던 코드보다 훨씬 간결하고 효율성이 높다

license_plate = list(input())

if license_plate[0] == 'd': # 첫 문자가 'd'인 경우
    answer = 10
else: # 첫 문자가 'c'인 경우
    answer = 26

for i in range(1, len(license_plate)):
    if license_plate[i-1] == 'c': 
        if license_plate[i] == 'c':
            answer *= 25 # cc처럼 연속된 경우
        else:
            answer *= 10 # 연속되지 않았다면 그냥 곱하면 됩ㄴ다
    elif license_plate[i-1] == 'd':
        if license_plate[i] == 'c':
            answer *= 26
        else:
            answer *= 9
print(answer)