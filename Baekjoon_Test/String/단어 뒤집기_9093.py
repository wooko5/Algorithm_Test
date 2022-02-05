test_case = int(input())
for _ in range(test_case):
    sentence = list(input().split())
    for i in range(len(sentence)):
        print(sentence[i][::-1], end=' ') # [::-1]은 원본을 복사해서 역순으로 만든 것을 의미한다