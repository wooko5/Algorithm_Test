from itertools import permutations
def isPrime(number): # 소수인지 아닌지 체크하는 함수
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def solution(numbers): # 내가 만들고 제출한 코드, 정답처리지만 더 효율화시킬 수 있을듯
    arr, array, result = [], [], [] # 시간복잡도가 O(N)
    for i in numbers: # 하나씩 배열에 넣기 
        arr.append(i) # numbers = "17" --> arr = ["1", "7"]
    for i in range(1, len(arr)+1): # 1부터 자기 자신 숫자까지 순열을 알아내기 위해
        array += list(map(''.join, permutations(arr, i))) # arr을 i(1, 2, 3..)의 순열 리스트(array) 만들기
    for i in array: # array의 원소들을 순회하면서
        if isPrime(int(i)): # 만약에 정수로 바꾼 원소가 소수라면
            result.append(int(i)) # 정답에 삽입
    return len(set(result)) # result 중에 중복이 있을 수도 있으니 중복된 것만 삭제하고 길이를 반환

def solution2(numbers): # 내꺼보다 더 짧고 시간복잡도가 좋은 다른 사람코드
    answer = []
    for i in range(1, len(numbers)+1): # 1부터 자기 자신 숫자까지 순열을 알아내기 위해
        perlist = list(map(''.join, permutations(list(numbers), i))) # arr을 i(1, 2, 3..)의 순열 리스트(perlist) 만들기
        for j in list(set(perlist)): # 순열 리스트(perlist)의 원소를 하나씩 순회하면서
            if isPrime(int(j)): # 만약에 정수로 바꾼 원소가 소수라면
                answer.append(int(j)) # 정답에 삽입
    return len(set(answer)) # answer 중에 중복이 있을 수도 있으니 중복된 것만 삭제하고 길이를 반환


numbers = "17"
print(solution(numbers))