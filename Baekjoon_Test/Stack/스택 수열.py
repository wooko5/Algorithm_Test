import sys
input = sys.stdin.readline
n = int(input())
stack = []
answer = []
count = 1

for _ in range(n): # n(데이터 개수)만큼 반복
    num = int(input())
    while count <= num: # 입력 받은 데이터에 도달할 때까지 삽입(push) 
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == num: # 스택의 최상위 원소가 데이터와 같을 때 출력(pop)
        stack.pop()
        answer.append('-')
    else: # 같지 않은 경우 
        print('NO')
        exit(0)
print('\n'.join(answer))