dic = dict()
for _ in range(int(input())):
    number = int(input())
    if number in dic: # (카드값 : 카드 개수)로 저장함
        dic[number] += 1 # 이미 있다면 카드 개수만 +1
    else:
        dic[number] = 1 # 없다면 새로 key:value 생성
dic = sorted(dic.items(), key = lambda x : (-x[1], x[0])) # 카드 개수를 내림차순 정렬하고 같은 개수의 카드는 오름차순 정렬
print(dic[0][0])
# import operator # 이 방법도 알아두자
# dic = sorted(dic.items(), key = operator.itemgetter(1)) # 1이면 카드 개수 즉 두번째 인자를 중심으로 오름차순 정렬