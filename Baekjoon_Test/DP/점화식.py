n = int(input())
MAX = 35+1
#그대로 구현만 하면 되는 생각보다 쉬운 문제였다
def jump(num):
    t = [0 for index in range(MAX)]
    t[0] = 1
    for i in range(1, MAX):
        for j in range(i):
            t[i] += t[j]*t[i-1-j]

    return t[num]

print(jump(n))