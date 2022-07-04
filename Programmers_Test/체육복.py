def solution(n, lost, reserve):
    reserve_n = list(set(reserve) - set(lost)) # 초기에 set()처리를 안 해줘서 75점밖에 안 나왔음
    lost_n = list(set(lost) - set(reserve)) # set을 통해 중복을 제거해서 차집합형태로 리스트를 생성
    answer = n - len(lost_n) # 이유: 도둑맞은 학생과 여벌의 옷을 가진 학생이 같을 수도 있기 때문이다
    
    for i in lost_n:
        if i + 1 in reserve_n:
            answer += 1
            reserve_n.remove(i + 1)
        
        elif i - 1 in reserve_n:
            answer += 1
            reserve_n.remove(i - 1)
    return answer

n = 5
lost = [2, 4]
reserve = [2, 4]
print(solution(n ,lost, reserve))