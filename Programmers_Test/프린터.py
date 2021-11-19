"""
첫 시도는 10점이었다, 두 번째 시도는 알바펫과 break문을 넣은 점수는 30점, 
알파벳없이 세번째 시도에 100점맞음
문제 대한 원리는 두 번째 시도와 같았으나 
두 번째 시도 때는 
import string
upper = [i for i in string.ascii_uppercase]를 이용했다 
근데 이렇게 하다보면 직관적으로 배열을 짤 수는 있지만 공간복잡도가 떨어지고 
알파벳과 실제 priorities의 인덱스가 달라질 수 있으므로 문제가 있는 것 같다
2021.07.29
"""
def solution(priorities, location):
    array = []
    result = []

    for i in range(len(priorities)):
        array.append([priorities[i], i]) # [중요도, 인덱스]를 가진 튜플같은 배열 생성
    
    while array:
        check = True
        priority, index = array.pop(0)
        
        for p in array:
            if p[0] > priority:
                array.append([priority, index])
                check = False
                break
        if check:
            result.append([priority, index])
    
    for i in range(len(result)):
        if result[i][1] == location:
            return i+1


priorities = [2, 1, 3, 2]
location = 2
#priorities= [1, 1, 9, 1, 1, 1]	
#location = 0
print(solution(priorities, location))