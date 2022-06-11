import sys; input = sys.stdin.readline
n = int(input())
answer = []
array = []
for i in range(n):
    array.append((int(input()), i)) # (숫자, index)을 쌍으로 해서 배열에 삽입
array_sort = sorted(array) # 숫자를 기준으로 오름차순 정렬

for i in range(n):
    answer.append(array_sort[i][1] - array[i][1]) # 정렬 배열 index - 정렬 안한 배열 index = 이동한 길이
print(max(answer)+1) # 이동한 길이가 가장 긴 index에 + 1한게 최대값이 버블정렬이 몇회차까지 필요한지를 나타냄