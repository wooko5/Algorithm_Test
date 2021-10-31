def solution(name):
    # 상하조정으로 알파벳 바꾸기
    alphabet = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name] # 알바벳 바꾸기 위한 횟수 배열
    index, answer = 0, 0
    
    while True:
        answer += alphabet[index]
        alphabet[index] = 0
        
        # 값이 0이면 알파벳을 바꿀 필요가 없는 것 들이다. 이외에는 answer에 해당 값을 더한다.
        if sum(alphabet) ==0:
            break
        
        # 좌우 이동방향 정하기, 좌우로 이동 방향을 정할 때 바꿔야하는 알파벳이 나오기까지 가장 짧은 거리를 구한다 (부분해)
        left, right = 1, 1
        while alphabet[index - left] ==0: # 'A'가 있다면 chage[]에 0으로 뜬다
            left +=1
        while alphabet[index + right] ==0: # 'A'가 있다면 chage[]에 0으로 뜬다
            right +=1
        
        # 위치조정        
        answer += left if left < right else right
        index += -left if left < right else right
    return answer

name = "JAZ"
print(solution(name))