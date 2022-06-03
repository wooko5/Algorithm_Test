grade_card = dict()
for _ in range(int(input())):
    name, korean, english, math = input().split()
    grade_card[name] = (int(korean), int(english), int(math))
grade_card = sorted(grade_card.items(), key = lambda x : (-x[1][0], x[1][1], -x[1][2], x[0]))
# '-x[1][0]'은 국어 내림차순, 'x[1][1]'은 영어 오름차순, '-x[1][2]'은 수학 내림차순, 'x[0]'은 이름 오름차순
for i in range(len(grade_card)):
    print(grade_card[i][0])