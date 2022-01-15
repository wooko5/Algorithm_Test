car_plate = input()
result = 0
for i in range(len(car_plate)):
    if i == 0: # 첫 문자에 따라 달라지는 할당값
        if car_plate[i] == "c":
            result += 26
        else:
            result += 10
        continue # 이게 핵심이다
    
    if car_plate[i] == car_plate[i-1]: # 문자가 연속으로 같은 경우
        if car_plate[i] == "c":
            result *= 25
        else:
            result *= 9
    else:
        if car_plate[i] == "c":
            result *= 26
        else:
            result *= 10
print(result)
