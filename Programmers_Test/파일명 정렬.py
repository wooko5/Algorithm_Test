"""
첫 시도: 20점
두번째 시도: 25점
5번째 시도만에 100점 나왔다 휴우
index를 건드리는 접근을 하다보니 계속 런타임오류가 나서
인터넷에서 힌트를 보고 문자열 자체로 가져왔다 
처음에는 head는 쉽게 구했지만, number를 인덱스 없이 어떻게 가져올까 하다가
string[len(head): ]가 number의 시작부터 문자열 끝까지 임을 알 수 있었다
정말 좋은 문제고, 오랜만에 머리써서 행복했다 ㅎㅎㅎㅎ
TMI: 대소문자 구분 없이 소팅 = a.sort(key=str.lower)
2021.07.22
"""

def solution(files):
    array = []

    for string in files:
        head = ''
        for char in string: # head를 구하기 위한 반복문
            if char.isdigit():
                break
            head += char # 숫자가 오기 전까지 head이므로 계속 문자를 추가한다

        number = ''
        for char in string[len(head):]: # number를 구하기 위한 반복문, head의 마지막 인덱스의 다음부터 끝까지
            if not char.isdigit():
                break
            number += char # 숫자는 number이므로 다른 문자가 오기 전까지 추가해준다

        array.append([head, number, string[len(head)+len(number): ]])
    
    array = sorted(array, key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(string) for string in array]
        

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))