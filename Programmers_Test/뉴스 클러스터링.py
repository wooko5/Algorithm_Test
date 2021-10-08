
"""
오랜만에 풀어보는 카카오 구현문제였다. 처음에 시도할 때는 70점이어서 고민끝에 인터넷으로 힌트를 참조했고,
Counter라는 자료형을 쓰는 것을 알게 되었다. 예전에도 문자열이나 배열에서 각 문자가 몇 개 있는지 알려주는 용도로
써봤는데 응용하는 방법을 알게 되었다. 앞으로도 문자열 처리에서 자주 쓰일 것 같다.
또한, set()같은 집합형 자료구조를 이용해서 다양한 집합을 만들어 낼 수 있음을 깨닫게 되었다.
Counter와 set(), dict()를 이용한 문제를 더 많이 봐야겠다.
프로그래머스 level2, 2021.10.08
"""
from collections import Counter

def calculator(number):
    return int(number*65536)

def solution(str1, str2):
    str1_uppper = str1.upper() # 문자열을 모두 대문자로 처리한 문자열
    str2_uppper = str2.upper()
    processed_array1 = []
    processed_array2 = []
    
    for i in range(len(str1_uppper)-1): # 공백, 숫자, 특수 기호 등 알파벳을 제외한 문자가 없는 순수 알파벳 2문자씩으로 된 배열 생성 1
        if str1_uppper[i].isalpha() and str1_uppper[i+1].isalpha():
            processed_array1.append(str1_uppper[i] + str1_uppper[i+1])
            
    for j in range(len(str2_uppper)-1): # 공백, 숫자, 특수 기호 등 알파벳을 제외한 문자가 없는 순수 알파벳 2문자씩으로 된 배열 생성 2
        if str2_uppper[j].isalpha() and str2_uppper[j+1].isalpha():
            processed_array2.append(str2_uppper[j] + str2_uppper[j+1])
            
    if not processed_array1 and not processed_array2: # 합집합과 교집합 모두 공집합인 경우 1을 반환
        return calculator(1)
    
    Counter1 = Counter(processed_array1) # Counter(딕셔너리 같은 자료구조)로 만들기
    Counter2 = Counter(processed_array2)
    
    intersect = list((Counter1 & Counter2).elements()) # 집합 자료형(set)처럼 사용 가능, 교집합 만들기 위해 elements()로 키값 추출
    union = list((Counter1 | Counter2).elements()) # 집합 자료형(set)처럼 사용 가능, 합집합 만들기 위해 elements()로 키값 추출
    
    return calculator(len(intersect) / len(union))