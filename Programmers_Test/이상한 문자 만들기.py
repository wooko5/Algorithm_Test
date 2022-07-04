"""
처음에 그냥 전체 문자열의 index로 구분하는줄 알았지만 
알고보니 단어마다 짝홀을 나눠서 짝수면 대문자, 홀수면 소문자를 출력하는 문제였다
공백이 나올때마다 count를 -1로 초기화 시키고, 만약에 문자가 나오면 0부터 시작해서 대문자/소문자를 만든다
매우 매우 쉬운 문제였다 역시나 level-1이라서 그런 것 같다 
2021.07.29
"""

def solution(s):
    answer = ''
    count = -1 # 공백이 아닌 단어 문자열이 나오는 것을 알려주는 기준
    for i in range(len(s)):
        if s[i].isalpha(): # 문자라면(숫자나 공백제외)
            count += 1
            if count % 2 == 0: 
                answer += s[i].upper() # 대문자를 정답 문자열에 합친다
            else:
                answer += s[i].lower() # 소문자를 정답 문자열에 합친다
        else:
            count = -1
            answer += s[i] # 공백도 들어가야함
    return answer


s = "try hello world"
print(solution(s))