def solution(number, k): # 정답, 스택을 이용했음 시간복잡도 O(len(number)) == O(N)이다
    # 1. 스택 생성
    stack = []

    # 2. 큰 수가 앞자리가 되게끔 스택에 저장합니다.
    for num in number: # number = "1924"라면 num은 "1", "9", "2", "4" 한 개씩 순회함
        while stack and stack[-1] < num and k > 0: # stack이 비어있지않고, stack의 가장 윗부분(마지막 원소)가 num보다 작고, k가 0보다 클때
            stack.pop() # stack 가장 윗부분을 추출(마지막 원소)
            k -= 1
        stack.append(num) # stack에 이어 붙이기
    print(stack) # stack = ['9', '4']
    print(k) # k는 0
    
    # 3. k가 남았다면 뒤에서부터 stack의 문자를 뺍니다.
    while k > 0:
        stack.pop()
        k-=1 # 만약에 k가 4라면 4만큼 stack 뒤에서 뺌
    return "".join(stack)


from itertools import combinations
def solution1(number, k): # 논리는 맞지만 시간복잡도에서 걸림 33점, 시간복잡도가 O(N^2)이라서 그런듯
    temp = 0
    result = [] # number = "1924", k = 2
    numbers = list(combinations(number,len(number)-k)) # 조합들을 리스트형태로 저장
    for i in range(len(numbers)): # i = 0 ~ 5
        answer = ''
        for j in range(len(number)-k): # j = 0, 1
            answer += numbers[i][j] # answer = "19", "12", "14"
        num = int(answer)
        if num >= temp: # 19, 24, 94 등
            result.append(num)
            temp = num
    return str(max(result))


def solution2(number, k): # 정답, 하지만 스택을 이용한게 더 쉬워서 참고용으로 둠
    collected = []
    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop() # collected의 가장 맨 뒤의 원소를 제거합니다.
            k -= 1 # k를 1씩 줄이기 
        if k == 0:
            collected += number[i:] # k가 0이라면 numbers 인덱스 i부터 끝까지 collected에 이어 붙이고 for문을 탈출
            break
        collected.append(num) # 순회 수 num을 collected 맨 뒤에 넣습니다.
    collected = collected[:-k] if k > 0 else collected # k가 0보다 크다면 collected를 뒤에서 k개 자릅니다.
    return  "".join(collected)


number = "18249"	
k = 3
print(solution(number, k))