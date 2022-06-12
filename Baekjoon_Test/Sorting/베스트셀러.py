import operator
total_books = int(input())
books = {}
answer = []

for _ in range(total_books):
    book = input()
    if book not in books: # 해당 책이 한번도 등장한 적이 없다면
        books[book] = 1 
    else: # 해당 책이 기존에 등장한 적이 있다면
        books[book] += 1

target = max(books.values())

for book, number in books.items(): # 딕셔너리의 key와 value를 동시에 호출하는 함수 dict.items()
    if number == target: # 최대 판매량과 같은 책이 있다면
        answer.append(book) # 정답 리스트에 추가

print(sorted(answer)[0]) # 최다 판매 책이 여러개이면 사전 순으로 가장 앞에 있는 원소를 출력