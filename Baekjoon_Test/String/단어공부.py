word = []
word = input()

alpha = ['A', 'B', 'C' 'D', 'E', 'F', 'G', 
'H', 'I', 'J', 'K', 'L' ,'M', 'N' ,'O' ,'P' ,'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X','Y','Z']

beta = ['a', 'b', 'c' 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l' ,'m', 'n' ,'o' ,'p' ,'q',
'r', 's', 't', 'u', 'v', 'w', 'x','y','z']

count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in word:
    for a_number in range(len(alpha)):
        if i == alpha[a_number]:
            count[a_number] += 1

for i in word:
    for b_number in range(len(beta)):
        if i == beta[b_number]:
            count[b_number] += 1


max_number = max(count)
truck = 0
for a in count:
    if max_number == a:
        truck +=1

if truck == 2:
    print('?')
else:
    print(alpha[count.index(max_number)])


#voca = list(input().upper())                          #input 값을 모두 대문자 리스트로 반환
 
#al_list = [0] * 26                                    #알파벳 수 만큼 리스트 생성
 
#for i in voca:
#    al_list[ord(i) - 65] += 1                         #input 값을 for문으로 돌려서 아스키코드에 대입해 A=0, B=1식으로 치환
                                                      #그 후 알파벳 자릿수에 해당하는 인덱스에 1씩 더함
#if al_list.count(max(al_list)) >= 2:                  #알파벳 리스트에서 가장 많이나온 수가 2개 이상이면
#    print('?')
#else:
#    print(chr(al_list.index(max(al_list)) + 65))      #알파벳 리스트에서 가장 큰 값의 인덱스 위치를 아스키코드로 변환하여 
                                                      #대문자 알파벳으로 바꾼후 출력
