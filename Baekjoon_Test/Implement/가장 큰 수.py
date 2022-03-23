numbers = [6, 10, 2]
# 1000이하의 조건이라면 x*3을 해줘야 하고, 10000이하의 조건이라면 x*4를 해줘야한다
# lambda x : x*3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다. 
# x*3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
# 이 문제의 핵심이라고 할 수 있다. 
# 문자열 비교는 ASCII 값으로 치환되어 정렬된다. 따라서 666, 101010, 222의 첫번째 인덱스 값으로 비교한다. 
# 6 = 86, 1 = 81, 2 = 82 이므로 6 > 2 > 1순으로 크다. 
# sort()의 기본 정렬 기준은 오름차순이다. reverse = True 전의 sort된 결과값은 10, 2, 6이다. 
# 이를 reverse = True를 통해 내림차순 해주면 6,2,10이 된다. 이것을 ''.join(num)을 통해 문자열을 합쳐주면 된다. 
# int로 변환한 뒤, 또 str로 변환해주는 이유?
#모든 값이 0일 때(즉, '000'을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다. 

def solution(numbers): 
    numbers = list(map(str, numbers)) # 문자열 리스트로 변형
    numbers.sort(key = lambda x:x*3, reverse = True) # 세자리 수를 기준으로 
    return str(int(''.join(numbers)))
print(solution(numbers))