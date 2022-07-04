# 대표적인 DP문제이다
# 두 수열의 길이가 N 미만일때, 시간복잡도는 O(N^2)로 문제 해결할 수 있다
# 만약에 처음 했던 방법인 '모든 문자를 비교'하면 O(2^N*2^M)이므로 불가능하다(N은 첫번째 문자열길이, M은 두번째 문자열길이)
string1 = input() # 첫번째 문자열
string2 = input() # 두번째 문자열
matrix = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]
#첫번째와 두번째 문자열 길이 + 1 만큼씩 이중배열 생성하고 0으로 초기화하기

for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]: # 만약에 두 문자열의 비교 문자가 같다면 
            matrix[i+1][j+1] = matrix[i][j] + 1 # 현재 위치(matrix는 문자열+1 이므로)의 값은 좌대각선 값+1이 된다
        else: # 만약에 두 문자열의 비교 문자가 같지 않다면
            matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j]) # 값은 현재 위치값의 왼쪽 또는 위쪽 값중에 큰 것을 넣는다
print(matrix[len(string1)][len(string2)]) # 이중배열의 가장 마지막 원소를 출력한다 == 제일 큰 값