"""
간단한 구현만 하면 되는거라서 직관적으로 뒤에서부터 필요한 4자리 숫자를 넣고, 나머지는 
"*"로 처리하고 역순으로 출력했다
2021.08.06
"""

def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-1, len(phone_number)-5, -1):
        answer += phone_number[i]
    for _ in range(len(phone_number)-4):
        answer += "*"
    return answer[::-1]