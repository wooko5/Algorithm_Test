import math

def calculation(x2, y2, z2, x1, y1, z1): # 두 점 사이의 거리를 구하는 함수
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

ax, ay, az, bx, by, bz, cx, cy, cz = map(float, input().split())
mx, my, mz = bx - ax, by - ay, bz - az # a와 b 사이의 중간 좌표들(x, y, z)
left, right, middle = 0.0, 1.0, 0

while True:
    if abs(right - left) < 1e-9: # right와 left의 차이가 0.000001보다 작으면 break, 문제에서 주어졌기 때문 
        middle = (left + right) / 2.0
        break
    
    m1 = left + (right - left) / 3.0
    m2 = right - (right - left) / 3.0
    # print(m1, m2, 'm 시리즈')
    fx = ax + mx * m1
    fy = ay + my * m1
    fz = az + mz * m1
    # print(fx, fy, fz, 'f시리즈')
    sx = ax + mx * m2
    sy = ay + my * m2
    sz = az + mz * m2
    # print(sx, sy, sz, 's시리즈')
    a = calculation(cx, cy, cz, fx, fy, fz)
    b = calculation(cx, cy, cz, sx, sy, sz)

    if a > b: # b가 a보다 작다면 => c와 a 사이의 거리가 c와 b 사이의 거리보다 짧다
        left = m1 # left값을 m1으로 갱신함 => b쪽으로 옮기기
    else:
        right = m2 # right값을 m2으로 갱신함 => a쪽으로 옮기기

answer = calculation(cx, cy, cz, ax + mx*middle, ay + my*middle, az + mz*middle)
print("%.10f"%answer)   