total_home, wifi = map(int, input().split())
home = []
for _ in range(total_home):
    home.append(int(input()))

home.sort()
min_gap = home[1] - home[0] # start
max_gap = home[-1] - home[0] # end

while min_gap <= max_gap:
    mid = (max_gap + min_gap) // 2
    value = home[0] # 가장 첫번째 원소
    count = 1
    for i in range(1, len(home)):  # 두번째 원소부터 끝까지
        if home[i] >= value + mid: # 만약 집의 위치가 value+mid(와이파이 거리) 보다 크거나 같다면, 공유기 설치가 가능하다는 이야기
            count += 1             # 공유기를 설치하므로 count값을 +1 해주고
            value = home[i]        # value를 공유기를 설치한 집 위치를 기준잡기
    if count >= wifi:              # 설치 가능한 공유기 개수가 wifi보다 작으면 max_gap을 감소시킨다
        min_gap = mid + 1
        answer = mid
    else:
        max_gap = mid - 1
print(answer)