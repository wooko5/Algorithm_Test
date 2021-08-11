"""
def solution(clothes): // 나중에 key의 value로 []을 넣고 싶을 때 쓸 코드 
    dic = dict()
    for i in range(len(clothes)):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = [clothes[i][0]]
        else:
            dic[clothes[i][1]].append(clothes[i][0])
    return dic 

T.C 첫번째꺼만 계속 시간 초과가 나서 왜 그럴까 생각하다가 인터넷을 보고 내가 생각한 경우의 수에서 +1
한 힌트를 참조해서 코드 안 보고 맞추게 되었다. 
처음 접근 자체는 좋았다. 옷종류를 key, 같은 옷 종류의 개수를 value로 저장
만약에 내가 입을 옷이 2종류(상의, 하의)고, 상의 2개, 하의 1개라고 하자.
내가 상의 선택 시 경우의 수는 2개가 아니라 3개다. 왜냐하면
[상의a, 상의b, 상의c, 상의를 선택 안 한 경우] 이렇게 4가지가 가능하기 때문이다.
그래서 각 key마다 value를 (value+1)로 지정하고
마지막 최종 경우의 수에서 모든 종류의 옷을 걸치지 않은 1가지 경우를 제외하기 때문에  
answer - 1 을 반환한다
"""
def solution(clothes):
    dic = dict()
    answer = 1

    for i in range(len(clothes)):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = 1
        else:
            dic[clothes[i][1]] += 1
    
    for value in dic.values():
        answer *= (value+1)

    return answer - 1 