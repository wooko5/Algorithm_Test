"""
dfs/bfs 문제
dfs 구현에만 정신이 팔려서 원리에 집중하지 못 했던 것 같다 
굉장히 쉬운 원리였는데 제대로 된 힌트가 없어서 구현하기 힘들어서 코드를 참조했다
다음부터는 좀더 생각해봐야겠다 2021.06.28
"""

def dfs(numbers, target, index):
    global count
    
    if index < len(numbers):
        numbers[index] *= 1 # 양수(+)로 만들기 
        dfs(numbers, target, index+1) # 다음 인덱스에 존재하는 numbers 원소에 접근하기 위함

        numbers[index] *= -1 # 음수(-)로 만들기
        dfs(numbers, target, index+1) # 다음 인덱스에 존재하는 numbers 원소에 접근하기 위함
    
    elif sum(numbers) == target: # index가 numbers의 전체 길이만큼 다 순회했다면
        count += 1 # 그중에 합이 target이 있다면 count + 1 해준다 

def solution(numbers, target):
    dfs(numbers, target, 0) # 0 인덱스부터 차례대로 순회
    return count # 최종 count 값을 반환 

count = 0
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))