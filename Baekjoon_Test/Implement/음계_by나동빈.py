A = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(len(A)-1):
    if A[i]>A[i+1]:
        ascending = False
    elif A[i]<A[i+1]:
        descending = False

if ascending: print('ascending')
elif descending: print('descending')
else: print('mixed')