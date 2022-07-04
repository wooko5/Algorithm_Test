def solution(answers):
    answer = []
    count1 = count2 = count3 =  0
    student1 = [1,2,3,4,5]*10000 # 총 5개 반복
    student2 = [2,1,2,3,2,4,2,5]*10000 # 총 8개 반복
    student3 = [3,3,1,1,2,2,4,4,5,5]*10000 # 총 10개 반복
    for index in range(len(answers)):
        if answers[index] == student1[index]:
            count1 += 1
        if answers[index] == student2[index]:
            count2 += 1
        if answers[index] == student3[index]:
            count3 += 1

    answerForTest = [count1, count2, count3]
    for student, score in enumerate(answerForTest):
        if score == max(answerForTest):
            answer.append(student+1)
    return answer