N, B = int(input()), list(map(int, input().split()))
#A = list()
#A.append(B[0]) 로 하는 것보다 
A = [B[0]]  #하는게 더 빠르고 간결하다 

for num in range(1, N):
    A.append((num+1)*B[num]-sum(A))

for i in A:
    print(i, end=' ')