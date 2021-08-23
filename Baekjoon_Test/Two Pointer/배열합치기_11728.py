import sys
input = sys.stdin.readline
A, B = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
answer_list = A_list + B_list
answer = ' '.join(map(str, sorted(answer_list))) # join함수는 리스트의 문자열들을 합치는 역할
# 중복없이 정렬된 answer_list는 map()에 의해 str로 변환됐고 각각의 요소를 하나씩 띄어서 출력하기 위해
# ' '.join이라는 함수를 씀
# ''.join이면 공백없이 합쳐짐
print(answer)