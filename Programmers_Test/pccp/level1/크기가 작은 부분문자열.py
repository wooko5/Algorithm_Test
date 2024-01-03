def solution(t, p):
    answer = 0
    length = len(p)  # 기준 자리수
    for i in range(len(t) - length + 1):
        number = int(t[i : length + i])
        if number <= int(p):
            answer += 1
    return answer

t = "3141592"
p = "271"	
# result = 2
# t = "500220839878"
# p = "7"	
# result = 8
# t = "10203"	
# p = "15"
# result = 3
print(solution(t, p))