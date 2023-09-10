global count # 함수 밖에서 전역변수를 선언할 때는 해당 방식으로 선언하고 초기화한다.
count = 0

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


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))