"""
2020년 상반기에 자바로 풀어본 경험이 있지만 매우 처음본 문제 같았다
처음에는 시간효율성에 깊게 사로잡혀서 자꾸 협소하게 이해했지만 고민좀함 ㅂㄷㅂㄷ
결국 나만의 구현법으로 간단하게 해결했다
1. h가 정렬된 배열의 가장 마지막 원소로 갈 때까지 while반복문을 돌린다 
2. 논문을 h편 이상 인용된 원소만 찾아서 cnt + 1 해줌
3. for문을 통해 배열을 모두 돌면서 cnt값을 만들고, cnt가 h보다 크거나 같으면, answer에 저장
4. 1, 2, 3을 반복
5. 여기서 핵심은 cnt 최대값을 찾는게 아니라 h를 가장 크게 만들어주는 것을 찾는 것이다
2021.07.15
"""

def solution(citations):
    citations.sort()
    h = 0
    answer = 0
    while h != citations[-1]:
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                cnt += 1
        if cnt >= h:
            answer = h
        h += 1
    return answer

"""
def solution(citations): # 더 좋은 타인의 코드, 본받도록 하자 흑흑 ㅠㅅㅠ
    citations = sorted(citations)
    length = len(citations)
    for i in range(length):
        if citations[i] >= length - i:
            return length - i # l-i : i인덱스 값과 같거나 큰 수의 개수
    return 0
"""


citations = [3, 0, 6, 1, 5]
#citations =	[10, 100]
print(solution(citations))