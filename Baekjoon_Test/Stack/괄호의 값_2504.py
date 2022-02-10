"""
이 문제는 stack을 활용하여 풀수있는 문제이다.

지난번 글 처럼 스택을 사용하므로 list를 스택으로 이용한다.

알고리즘을 설명해보면 스택에 괄호를 여는 "(","[" 기호와 연산결과를 저장하는 방법으로 구현했다.

우선 이해를 쉽게하기 위해 연산결과를 저장하는 부분은 무시한 채로 코드를 보면

0. 입력받은 문자열을 순서대로 검사하면서

1. 괄호를 여는 기호의 경우에는 바로 스택에 push(append)연산을 해준다.

2. 그리고 괄호를 닫는 기호( ")" , "]" )를 만나면 자신에게 알맞는 괄호를 여는 기호를 만날때 까지 스택을 pop 해준다.

3. 이때 자신에게 맞지 않는 닫는기호를 만날경우 

ex) "]"일때 "("를 만난 경우 

    잘못된 입력이므로 0을 출력후 종료한다.

위의 규칙대로 동작한다.
여기에 괄호에 맞는 연산을 하기 위해서 스택에 연산 결과를 push하고 result라는 변수를 통해 연산을 해주는 부분을 추가했다.

우선 괄호 닫는 기호를 만날때 마다 나오는 연산 결과를 스택에 push 해준다.

ex) 입력이 "()()" 인 경우 스택에는 [2,2] 가 저장된다.

그리고 이를 마지막에 for문을 통해 모두 더하여 출력해준다. 

모두 더하는 이유는 문제의 규칙을 보면 결국 괄호가 '완전히' 닫힐때마다(=해당 연산값을 곱할 일이 더이상 없는 경우) 완료된 연산들의 합이 정답이기 때문이다.

그리고 연산값이 곱해져야할 상태이면 

ex) "(())"일때 스택의 상태가 ["(",2] 일때 ")"를 만났을때

이때 result라는 변수를 활용하여 기존에 저장되있던 값을 모두 더해주고 괄호안에 값에 괄호에 맞는 곱셈을 해준다.

ex) "(()())"일때 스택에는 ["(",2,2] 인 상황이 올것이고 이때 ")"를 만나면 스택의 "("를 만나기 전까지의 값들 (2,2)는 모두 더한 뒤에 괄호 닫기를 만났을때 모두 더한값(4) 에 *2 를 해준다. 
그리고 연산 결과를 스택에 다시 저장한다. 위의 알고리즘을 코드로 나타낸것이 다음과 같다.
"""
brackets = input() # 괄호는 1이상 30이하
stack = []
for i in brackets:
 
    if i == ')':
        result = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if result == 0:
                    stack.append(2)
                else:
                    stack.append(2 * result)
                break
            elif top == '[':
                print(0)
                exit(0)
            else: # top이 정수인 경우
                if result == 0:
                    result = int(top)
                else:
                    result += int(top)
 
    elif i == ']':
        result = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if result == 0:
                    stack.append(3)
                else:
                    stack.append(3 * result)
                break
            elif top == '(': # 성립하지 않는 조건이므로 0을 출력
                print(0)
                exit(0)
            else: # top이 정수인 경우
                if result == 0:
                    result = int(top)
                else:
                    result += int(top)
    
    else: # '(', '[' 인 경우 스택에 삽입
        stack.append(i)
 
answer = 0
for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        answer += i
print(answer)