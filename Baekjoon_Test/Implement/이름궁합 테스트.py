N, M = map(int, input().split())  # 8 14 처럼 숫자로 받기 때문에 문자열을 int형으로 바꿔주기 위해 map을 사용한다
A, B = input().split()            #LEESIYUN MIYA처럼 단어가 나와서 굳이 map으로 int형으로 안 해도 괜찮아서 이렇게 함 
number = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
AB = ''
min_len =min(N,M)    # 두 개의 숫자 중에서 더 작은 놈을 반환

for i in range(min_len):
    AB += A[i] + B[i]  #먼저 짧은 단어 기준으로 둘이서 섞고 

AB += A[min_len:] + B[min_len:]  #남은 단어처리, ':'의 의미는 A와 B중에 남은 긴 나머지를 반환하는 것 
lst = [number[ord(i)-ord('A')] for i in AB]  #AB는 L M E I E Y S A I W Y A U K N I S A K U R A
                                              #알파벳을 number의 숫자로 바꿀려고 하는 코드이다
for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]
print("{}%".format(lst[0]%10*10 + lst[1]%10))  #1, 2, 3의 방식을 간단화 시킨 방법이다