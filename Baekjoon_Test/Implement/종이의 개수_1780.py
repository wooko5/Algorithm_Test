n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt_m_uno = 0 # -1
cnt_cero = 0 # 0 
cnt_p_dos = 0 # 1


def check(x, y, n): # 범위 내의 색깔이 모두 동일한지 판단하는 함수
    color = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != color:
                return False
    return True

def solve(x, y, n):
    global cnt_m_uno, cnt_cero, cnt_p_dos

    if check(x, y, n):
        if matrix[x][y] == -1:
            cnt_m_uno += 1
        elif matrix[x][y] == 0:
            cnt_cero += 1
        else:
            cnt_p_dos += 1
        return
    else:
        n1 = n // 3
        n2 = (n // 3) * 2
        solve(x, y, n1)
        solve(x+n1, y, n1)
        solve(x, y+n1, n1)
        solve(x+n1, y+n1, n1)
        solve(x+n2, y, n1)
        solve(x, y+n2, n1)
        solve(x+n1, y+n2, n1)
        solve(x+n2, y+n1, n1)
        solve(x+n2, y+n2, n1)

solve(0, 0, n)
print(cnt_m_uno)
print(cnt_cero)
print(cnt_p_dos)