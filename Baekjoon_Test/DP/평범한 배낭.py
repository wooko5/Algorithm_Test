# 배낭문제(Knapsack Problem)으로 잘 알려진 DP의 전형적인 문제이다
# 시간복잡도는 O(N*K)를 갖는다 N은 물품의 수, K는 배낭에 담을 수 있는 무게
# 핵심 아이디어: 모든 경우의 수에 대해 최대 가치를 저장하기
# matrix[i][j] = 배당에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치, i는 물품 번호
# matrix[i][j] = matrix[i-1][j] or max(matrix[i-1][j], matrix[i-1][j-w[i]]+j[i])
N, K = map(int, input().split())
matrix = [[0 for _ in range(K+1)] for _ in range(N+1)]
w, v = [0], [0]

for _ in range(N):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)
    
for i in range(N+1):
    for j in range(K+1):
        if j < w[i]:
            matrix[i][j] = matrix[i-1][j]
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-w[i]]+v[i])
print(matrix)