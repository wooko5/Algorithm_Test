target = int(input()) # 가고싶은 채널
error_btn = int(input()) # 고장난 버튼의 개수
enable_set = {str(i) for i in range(10)}

if (error_btn == 0): # 리모컨의 고장이 없는 경우 
    pass
else:
    break_set = set(input().split()) # 고장난 버튼들
    enable_set -= break_set # 고장난 버튼을 제외한 정상 버튼만 set()에 남게 된다

result = abs(target - 100) # 100(기본 채널)부터 시작하기 때문에 목표 채널에서 100만큼 뺀다 
for number in range(1000001): # 모든 경우의 수를 보기 위해 0 ~ 100만까지의 숫자를 연산
    check = True
    for part_number in str(number): # 예를 들어, 5455가 number면 part_number는 '5', '4', '5', '5' 이다
        if part_number not in enable_set: # 각 자리 수가 허용된 숫자 집합에 없다면
            check = False  
            break # check를 False로 바꾸고 다음 숫자로 넘어가기
    if check == True: # 만약 우리가 찾는 숫자와 같거나 N과 비슷한 숫자라면
        result = min(result, abs(target - number) + len(str(number))) # N-number에 number의 버튼 개수만큼 더하기
print(result)