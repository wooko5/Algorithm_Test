"""
2021 카카오 채용연계형 인턴십에 나온 문제이다
그때는 정확하고 빠르게 못 푼 것 같은데 오늘은 간단하게 풀었다
s의 최대길이가 50밖에 되지 않기 때문에 index를 이용할 접근법을 고안했다
예를 들어, s가 "2three45sixseven"인 경우, 자연수는 문자 한 개만 봐도 변환이 가능한지 판명나기 때문에 
반복문 가장 처음 isdigit()을 이용해서 판별하고, 만약에 문자가 숫자라면 j값을 +1해준다
그리고 temp가 number배열에 있는 것 중에 똑같은 문자열이 있다면 answer에 추가하고, 
j의 위치를 현재 i위치로 옮긴다 왜냐하면 초기화 시켜주기 위함이다
다른 풀이를 보니깐 딕셔너리구조로 많이 풀던데 나도 나중에 그렇게 함 해봐야겠다
2021.07.24
"""
def solution(s):
    number = [['zero', '0'], ['one', '1'], ['two', '2'], ['three', '3'], 
    ['four', '4'], ['five', '5'], ['six', '6'], ['seven', '7'], ['eight', '8'], ['nine', '9']]
    answer = ''
    i = 1
    j = 0

    while i <= len(s):
        temp = s[j:i]
        if temp.isdigit():
            answer += temp
            j += 1
        else:
            for num in number:
                if temp == num[0]:
                    n = num[1]
                    answer += n
                    j = i
                    break
        i += 1
    return int(answer)


s = "2three45sixseven"
print(solution(s))