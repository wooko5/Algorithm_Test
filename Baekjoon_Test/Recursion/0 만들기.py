# 가능한 모든 경우의 수를 생각해서 연산자 리스트를 만들자
# 파이썬의 eval()을 이용해서 문자열 형식의 표현식을 만들자
import copy
def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array)) # deepcopy를 안 해주면 pop()때문에 
        return # 원소가 모두 빠져나간 공백 리스트만 반환함 그래서 deepcopy를 해줘야함
    array.append(' ') # [' ']을 넣은 상태
    recursive(array, n) # 또다시 재귀호출을 통해 [' ', ' '], [' ', '+'], [' ', '-']을 생성한다
    array.pop() # 그리고 나서 pop()을 함

    array.append('+')
    recursive(array, n)
    array.pop()
    
    array.append('-')
    recursive(array, n)
    array.pop()

test_case = int(input())
for _ in range(test_case):
    operators_list = [] # 연산자(공백, +, -)을 담을 리스트 생성
    N = int(input()) # 원하는 자연수 입력 
    recursive([], N-1) # []에 N-1만큼 재귀호출로 연산자 리스트 만들기
    # N-1인 이유는 N=3이면 1,2,3 이므로 1과2, 2와3 사이에만 연산자가 들어가므로 
    # 연산자가 개수는 N-1이 되어야함
    integers = [i for i in range(1, N+1)] # 1부터 N까지 자연수가 들어간 리스트 integers

    for operators in operators_list: # 연산자 리스트에서 하나씩 뽑아서 
        string = "" # 비어있는 문자열
        for i in range(N-1): # 0 ~ N-2까지 
            string += str(integers[i]) + operators[i] # 자연수와 연산자를 넣은 문자열 만들기 
        string += str(integers[-1]) # 마지막은 integers의 가장 마지막 자연수 넣기
        if eval(string.replace(" ", "")) == 0: # replace(" ", "")는 공백을 모두 지워버리는 기능이다
            print(string) # eval()로 연산한 결과가 0이면 문자열을 출력하기
    print("") # 한줄 띄기