"""
처음에는 어떻게 table을 나눌까 생각하다가 딕셔너리구조(해시테이블)를 이용해봤다 
하지만 전문분야만큼5개의 딕셔너리를 생성해야하기 때문에 너무 번거로운 것 같았고
split() 함수를 이용해서 table의 row 문자열을 각각의 column으로 나눌 수 있었다
이후에 선호도 점수가 있는 언어들을 따로 계산해주고, 나머지 언어는 0으로 곱해서 totalScore를 산정했다
비어있는 answer 배열에 [언어 총점수(totalScore), 언어이름(stringNew[0])]를 append하고
총점수를 lambda를 이용해서 역순으로 정렬, 총점수가 같다면 언어이름을 사전순으로 정렬해서 
가장 먼저 나온 배열의 언어이름을 반환한다. 
처음부터 split()함수를 생각했다면 더 빠르게 풀 수 있었을 것 같다. 초기 접근을 잘 하자!
2021.08.24 
"""
def solution(table, languages, preference):
    answer = []
    
    for string in table:
        stringNew = string.split()
        totalScore = 0
        
        for i in range(1, len(stringNew)): # 6 - i == 진짜 점수 
            score = 6 - i
            prefer = 0
            
            if stringNew[i] in languages:
                idx = languages.index(stringNew[i])
                prefer = preference[idx]
                
            totalScore += score * prefer
        answer.append([totalScore, stringNew[0]])
    answer = sorted(answer, key = lambda x : (-x[0], x[1]))
    return answer[0][1]