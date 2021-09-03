"""
계속 헤매었다 하하하 다른 분의 코드를 한줄씩 봐가면서 
결국 내손으로 맞춤 부분합격느낌?
큐를 이용한 다양한 문제들에 대해 풀어야봐야겠다
2021.07.15 
"""

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0]*bridge_length # [0, 0]짜리 큐를 만듦 

    while bridge:
        time += 1
        bridge.pop(0) # 큐를 pop(0)하면서 한 칸씩 트럭을 땡김
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight: # 다리위의 무게와 대기중인 버스의 무게를 합산해서
                truck = truck_weights.pop(0) # weight보다 적으면 다리위에 올리고
                bridge.append(truck)
            else: # 그게 아니라면 0을 추가해서 못 들어오게 한다
                bridge.append(0)
    return time


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))