"""
2020 카카오인턴 코테문제(구현)
작년에는 못 풀었지만 지금은 혼자서 참조없이 잘 풀었다 ㅠㅠ
처음에 버튼 간의 거리를 어떻게 계산할지 고민을 많이 하다가
오른손 위치 정보를 가진 배열 locate_right, 왼손 위치 정보를 가진 배열 locate_left를 생성하고
손가락 아래 숫자 정보와 우리가 누를 숫자의 차이를 구하고, 
그 결과값이 2보다 크다면 3으로 나눈 몫과 나머지를 더한게 최종 거리값이 된다!
예를 들어, 1과 8의 차이값은 7이고 실제 거리값은 7을 3으로 나눈 몫(2) + 나머지(1)이므로 둘을 합치면 3이 된다
이런 방식으로 왼손과 오른손에 대한 거리값을 생성해서 둘 중 더 가까운 쪽을 움직이고
둘의 거리가 같다면 왼손잡이, 오른손잡이를 고려해서 정답을 도출했다
또한 '*', 0, '#'은 10, 11, 12로 변환해서 풀었다
2021.07.22
"""

def calc(locate, target):
    if target == 0:
        target = 11
    elif target == '*':
        target = 10
    elif target == '#':
        target = 12
    if locate == 0:
        locate = 11
    elif locate == '*':
        locate = 10
    elif locate == '#':
        locate = 12
        
    result = abs(locate - target)
    if result > 2:
        result = result // 3 + result % 3
    return result

def solution(numbers, hand):
    locate_right = ['#']
    locate_left = ['*']
    answer = ''
    
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            locate_left.append(numbers[i])
        
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            locate_right.append(numbers[i])
        
        else:
            right = calc(locate_right[-1], numbers[i])
            left = calc(locate_left[-1], numbers[i])
            
            if right < left:
                answer += 'R'
                locate_right.append(numbers[i])
            
            elif right > left:
                answer += 'L'
                locate_left.append(numbers[i])
            
            else:
                if hand == 'left':
                    answer += 'L'
                    locate_left.append(numbers[i])
                else:
                    answer += 'R'
                    locate_right.append(numbers[i])
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
# 정답은 "LRLLLRLLRRL"