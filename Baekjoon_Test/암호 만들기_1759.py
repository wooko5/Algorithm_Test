from itertools import combinations
L, C = map(int, input().split()) # 4, 6
vowels = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트 
array = sorted(list(input().split())) # C개의 문자열을 배열로 만들고 정렬함
for password in combinations(array, L): # array의 문자들을 L개의 조합으로 추출한 모든 경우의 수, 이런 방식을 첨에 생각 못함
    count = 0 # 모음의 개수 세기
    for i in password:
        if i in vowels:
            count += 1
    if (count >= 1) and (count <= L - 2): # 모음이 최소 1개 이상 and 자음이 최소 2개 이상인 경우, 출력
        print(''.join(password))