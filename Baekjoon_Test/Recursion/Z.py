# 시간초과가 나옴
def solve(n, row, col):
    global count
    if n == 2: # 크기가 4x4(2^2 x 2^2) 행렬에서 
        if row == Row and col == Col: # 알려는 위치(row, col)가 입력한 위치(Row, Col)과 같다면
            print(count)
            return
        count += 1

        if row == Row and col + 1 == Col: # 알려는 위치(row, col + 1)가 입력한 위치(Row, Col)과 같다면
            print(count)
            return
        count += 1
        
        if row + 1 == Row and col == Col: # 알려는 위치(row + 1, col)가 입력한 위치(Row, Col)과 같다면
            print(count)
            return
        count += 1
        
        if row + 1 == Row and col + 1 == Col: # 알려는 위치(row + 1, col + 1)가 입력한 위치(Row, Col)과 같다면
            print(count) # 횟수를 출력하고 
            return
        count += 1
    # 행렬의 크기가 4x4(2^2 x 2^2)보다 큰 경우는 모두 재귀호출
    else:
        solve(n//2, row, col) # 호출할 때마다 행렬의 크기인 n은 절반으로 줄어들고
        solve(n//2, row, col + n//2) # 줄어든 만큼 row나 col을 움직여서 재귀호출한다
        solve(n//2, row + n//2, col)
        solve(n//2, row + n//2, col + n//2)

N, Row, Col = map(int, input().split())
count = 0 
solve(2**N, 0, 0) # 2의 n승 크기인 행렬에서 0행0렬부터 탐색시작하기