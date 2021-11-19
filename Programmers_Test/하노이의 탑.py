"""
인터넷에 있는 수많은 하노이탑 재귀함수 원리를 보고 
코드 참조없이 힌트로 작성했다 후우,,, 근데 마지막에 move()함수가 뭔지 싶어서 이건 봄 ㅠㅠ
잘했지만 더 열심히 공부해야겠다
2021.07.27
"""

def hanoi(n, start, end, through, answer): # 원반의 개수 N을 start에서 출발, through를 거쳐서, end에 도착하는 함수
    if n == 1: # 옮길 원반이 1개면 그냥 옮겨주기면 하면 되기에
        answer.append([start, end]) # 원래는 print(start, '->' ,end)을 쓴다
    
    else:
        hanoi(n-1, start, through, end, answer) # A -> C -> B, 즉 A에서 B로 가는 경우
        answer.append([start, end]) # 원래는 print(start, '->' ,end)을 쓴다
        hanoi(n-1, through, end, start, answer) # B -> A -> C, 즉 B에서 C로 가는 경우
    
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer) # 1에서 출발, 2를 거쳐서 3에 도착하는 하노이의 탑 함수
    return answer


n = 2
print(solution(n))