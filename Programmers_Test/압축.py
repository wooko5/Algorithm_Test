"""
자바로 풀려다가 도저히 문자열을 맘대로 조작하는게 너무 길어져서 파이썬으로 하게 되었다.
확실히 간결한 코드 때문에 코테에서는 자바가 파이썬을 이기는 건 불가능해 보인다. 
아무튼 좀 더 '문제에 대한 규칙 파악'과 자바에 대한 이해를 높이고, 파이썬도 자주 풀어야겠다
2021.10.14
"""
def solution(msg):
    answer = []
    alphabet = {}

    for i in range(26):
        alphabet[chr(65+i)] = i+1 # {'A': 1, 'B': 2, 'C': 3, ..., 'Z': 26} 딕셔너리 생성

    w, c = 0, 1
    while True:
        if c == len(msg): # c가 문자열의 마지막까지 왔다면
            answer.append(alphabet[msg[w : c]]) # w ~ c-1까지 문자열을 정답 배열에 추가 
            break

        if msg[w : c + 1] not in alphabet: # w ~ c의 두 글자가 알파벳 딕셔너리에 없다면 
            alphabet[msg[w : c + 1]] = len(alphabet) + 1 # 알파벳 딕셔너리에 w + c의 두 글자 추가
            answer.append(alphabet[msg[w : c]]) # w ~ c-1까지 문자열을 정답 배열에 추가 
            w = c

        c += 1
    return answer