# 주어질 문자열의 길이가 최대 100만이므로 단순한 구현으로는 힘듦
# 스택을 이용한다
# 왼쪽 스택과 오른쪽 스택 사이에 커서가 있다고 생각하자
test_case = int(input())

for _ in range(test_case):
    password = input()
    left_stack = [] 
    right_stack = []

    for character in password:
        if character == '<': # '<'가 오면 left_stack의 최상위 요소를 pop해서 right_stack에 삽입
            if left_stack:
                right_stack.append(left_stack.pop())
        elif character == '>': # '>'가 오면 right_stack의 최상위 요소를 pop해서 left_stack에 삽입
            if right_stack:
                left_stack.append(right_stack.pop())
        elif character == '-': # '-'가 오면 left_stack의 최상위 요소 삭제
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(character) # 나머지 문자들은 다 left_stack에 삽입
    left_stack.extend(reversed(right_stack)) # left_stack에 right_stack를 거꾸로 한 걸 extend해서 합침
    print(''.join(left_stack)) 