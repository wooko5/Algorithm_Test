N, M = map(int, input().split())  # 8 14 처럼 숫자로 받기 때문에 문자열을 int형으로 바꿔주기 위해 map을 사용한다
A, B = input().split()            #LEESIYUN MIYA처럼 단어가 나와서 굳이 map으로 int형으로 안 해도 괜찮아서 이렇게 함 


#alpha = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
number = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
min_len =min(N,M)    # 두 개의 숫자 중에서 더 작은 놈을 반환
for i in range(min_len):
    AB += A[i] + B[i]  #먼저 짧은 단어 기준으로 둘이서 섞고 

AB += A[min_len:] + B[min_len:]  #남은 단어처리, ':'의 의미는 A와 B중에 남은 긴 나머지를 반환하는 것 

lst = [number[ord(i)-ord('A')] for i in AB]  #AB는 L M E I E Y S A I W Y A U K N I S A K U R A
                                              #알파벳을 number의 숫자로 바꿀려고 하는 코드이다
#print(lst) #L M E I E Y S A I W Y A U K N I S A K U R A의 초기상태 [1, 3, 4, 1, 4, 2, 1, 3, 1, 1, 2, 3, 1, 3, 2, 1, 1, 3, 3, 1, 2, 3]가 나온다

for i in range(N+M-2):        #계속해서 더한 값을 구해서 최종 궁합확률을 알려주는 코드 
                              #2를 빼는 이유는 마지막 '27%'처럼 2개를 남겨야해서 
    for j in range(N+M-1-i):  #-1은 index 때문  
        lst[j] += lst[j+1]
#       lst[j] %= 10  #---1

#if lst[0] == 0:
#    print(lst[1],'%') #---2

#else:
#    print(lst[0]*10+lst[1],'%') #---3

print("{}%".format(lst[0]%10*10 + lst[1]%10))  #1, 2, 3의 방식을 간단화 시킨 방법이다

#다른 방법, 함수로 짜는 방식!
def fuction(lst):
    ret = []
    for i in range(lst-1):
        ret.append((lst[i]+lst[i+1])%10)
    return ret 