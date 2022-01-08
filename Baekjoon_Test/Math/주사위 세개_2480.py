dice = sorted(list(map(int, input().split()))) # 처음부터 정렬해서 가져온다
if len(set(dice)) == 1:
    print(10000+(dice[0]*1000))
elif len(set(dice)) == 2: # 2개가 겹치면 (1, 2), (2, 3) 이렇게 겹치기 때문에 2는 무조건 겹친다 그래서 index는 1!
    print(1000+(dice[1]*100))
else:
    print(max(dice)*100)