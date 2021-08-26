"""
처음에는 아래와 같은 코드를 짜서 10점이 나왔다
생각해보니 arr배열의 각 원소는 0~9였고, 
그래서 테스크 케이스로 주어지지 않을 -1을 answer의 첫 원소로 넣었다.
def solution(arr):
    answer = [0]
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
    answer.pop(0)
    return answer

너무 간단했던 level1 문제였다
그래도 문제를 꼼꼼히 보는 습관을 꼭 가져야겠다!!
2021.08.03
"""

def solution(arr):
    answer = [-1]
    for num in arr:
        if answer[-1] != num: # answer의 가장 마지막 원소가 num가 같지 않다는 것은 
            answer.append(num) # 연속한 숫자들이 서로 다르다는 것
    answer.pop(0) # 연속한 숫자들을 제외한 정답배열을 만들고, 가장 앞에 있을 -1을 pop(0)한다
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))