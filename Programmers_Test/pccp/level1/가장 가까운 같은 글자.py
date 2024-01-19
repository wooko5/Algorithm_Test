def solution(s):
    answer = [-1]

    for i in range(1, len(s)):
        temp = []
        array = s[:i]

        for j in range(len(array)):
            if array[j] == s[i]:
                temp.append(i - j)

        answer.append(-1) if not temp else answer.append(min(temp))

    return answer
