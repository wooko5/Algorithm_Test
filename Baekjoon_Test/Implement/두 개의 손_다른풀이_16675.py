ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())
# 0은 가위, 1은 보, 2는 바위
# 0은 1을 이기고, 1은 2를 이기고, 2는 0을 이긴다
if ML == MR and (ML+2) % 3 in [TL, TR]: # '(ML+2) % 3'는 상대방이 낸 것을 이길 수 있는 경우를 말한다
    print('TK') # 예를 들어, 민성이의 양 손이 가위을 내고 태경이가 바위를 냈을 경우 == 태경이 승리
elif TL == TR and (TL+2) % 3 in [ML, MR]:
    print('MS')
else:
    print('?')