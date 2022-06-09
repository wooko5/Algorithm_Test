N = int(input())
array = [] 
for _ in range(N):
    data = input().split(' ') # 공백을 기준으로 나이와 이름 데이터를 가진 data 만들기
    array.append((int(data[0]), data[1])) # 리스트에 나이와 이름을 삽입, append는 인자가 한 개만 받을 수 있으므로 ()로 묶어주자
array = sorted(array, key=lambda x:x[0]) # x[0]은 array[0]즉 나이 기준으로 오름차순 정렬을 의미
for i in array:
    print(i[0], i[1]) # 나이와 이름을 출력