a, b, c, x, y = map(int, input().split())

if 2 * c < a + b: # 반반 2마리 가격보다 (양념1마리, 후라이드 1마리) 가격이 크다면
    temp = 2 * c
else: # 반반 2마리 가격보다 (양념1마리, 후라이드 1마리) 가격이 작다면
    temp = a + b

cnt = min(x, y) # 둘 중 최소 마리 수의 종류로 cnt 설정 
answer = temp * cnt

if x > y: # 양념의 개수가 후라이드 개수보다 많다면 
    answer += a * abs(x - y) # 남은 개수만큼 양념치킨 가격 더하기
elif x < y: # 양념의 개수가 후라이드 개수보다 적다면
    answer += b * abs(x - y) # 남은 개수만큼 후라이드치킨 가격 더하기

if answer < temp * max(x, y): # 최종 점검
    print(answer)
else: # 최종결과 값이 그냥 max에 temp 곱한것보다 크다면 출력
    print(temp * max(x, y)) 