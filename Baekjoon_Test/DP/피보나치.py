T = int(input())

zero = [1,0,1]
one = [0,1,1]

def fibonacci(number):
    length = len(zero)
    if length <= number:
        for i in range(length, number + 1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("%d %d" %(zero[number], one[number]) )

for i in range(T):
    N = int(input())
    fibonacci(N)