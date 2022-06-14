total_birds = int(input())
bird = 1
count = 0
while total_birds != 0: # total_birds이 0이면 남아있는 새가 없다는 뜻이므로 break
    if bird > total_birds: # 날아가는 새가 남아있는 새보다 많다면
        bird = 1 
    total_birds -= bird # 전체 새 - 날아간 새 = 남아있는 새
    bird += 1 # 1, 2, 3, 4 처럼 1씩 증가
    count += 1 
print(count)