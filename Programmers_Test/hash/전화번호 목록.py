"""
이 문제는 사실 해시문제지만 파이썬 라이브러리 함수를 써서 하는 편이 pythonic한 것 같다
zip이라는 함수를 통해 1대1 대응된 배열을 만들고, startswith를 써서 괄호에 든 문자로 시작하는지 알 수 있다
다음에 다시 한번 풀어봐야겠다 
2021.07.06
"""

def solution(phone_book):
    phone_book.sort()
    for base, target in zip(phone_book, phone_book[1:]):        
        if target.startswith(base):
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))


# 2022.10.02 다시 풀음
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True