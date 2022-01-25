N, row, col = map(int, input().split())
count = 0

# while문을 돌면서 해당 좌표(row, col)가 어디있는지 찾고 범위를 계속해서 줄여나감
""" 
예를 들어, 좌표가 3사분면에 있다면 1,2사분면은 지나온거니까 그 갯수만큼 더해줌 
-> 좌표가 1사분면에 있으면 지나온게 없으니까 더해줄 필요 X
범위를 줄여나갈때마다 좌표값을 temp만큼 빼줘야함
주의 사항: 번호는 0부터 시작!! $
"""
while N >= 1:
    temp = 2 ** (N - 1)

    if N == 1:
        if row is 0 and col is 1:  # 2사분면
            count += 1
        elif row is 1 and col is 0:  # 3사분면
            count += 2
        elif row is 1 and col is 1:  # 4사분면
            count += 3
        break

    if row < temp <= col:  # 2사분면
        count += temp ** 2
        col -= temp
    elif col < temp <= row:  # 3사분면
        count += (temp ** 2) * 2
        row -= temp
    elif temp <= row and temp <= col:  # 4사분면
        count += (temp ** 2) * 3
        row -= temp
        col -= temp
    N -= 1
print(count)