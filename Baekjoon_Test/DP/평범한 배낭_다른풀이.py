# 배낭문제(Knapsack Problem)으로 잘 알려진 DP의 전형적인 문제이다
# 시간복잡도는 O(N*K)를 갖는다 N은 물품의 수, K는 배낭에 담을 수 있는 무게
# 핵심 아이디어: 모든 경우의 수에 대해 최대 가치를 저장하기
# matrix[i][j] = 배당에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치, i는 물품 번호
# matrix[i][j] = matrix[i-1][j] or max(matrix[i-1][j], matrix[i-1][j-w[i]]+j[i])
N, K = map(int, input().split())
matrix = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int, input().split())
    for j in range(1, K+1):
        if j < weight:
            matrix[i][j] = matrix[i-1][j] # 바로 위 요소에서 value 가져오기
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-weight]+value) # 바로 위 요소에서 value VS 남는 무게만큼 더 넣을 수 있는 value + 현재 value
print(matrix[N][K])