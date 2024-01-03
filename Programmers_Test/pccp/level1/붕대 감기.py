def solution(bandage, health, attacks):
    time = 0  # 시간
    success = 0  # 연속 회복시간
    max_health = health  # 최대 HP량
    end_time = attacks[-1][0]  # 마지막 시간

    while time < end_time:
        time += 1
        attack_check = False  # 공격 여부

        if attacks[0][0] == time and attacks:
            health -= attacks[0][1]
            attacks.pop(0)
            success = 0
            attack_check = True

        if not attack_check:  # 공격을 받지 않았을 경우
            health = (max_health if health + bandage[1] >= max_health else health + bandage[1])  # 초당 회복력
            success += 1

            if success == bandage[0]:  # 시전시간 도달 시
                success = 0
                health = (max_health if health + bandage[2] >= max_health else health + bandage[2])  # 추가 회복
        
        print('time == ', time, 'health == ', health, 'success == ', success, 'attack_check == ', attack_check)
        if health <= 0:
            break
    return -1 if health <= 0 else health


# bandage = [5, 1, 5]
# health = 30
# attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]  # result = 5

# bandage = [3, 2, 7]
# health = 20
# attacks = [[1, 15], [5, 16], [8, 6]]  # result = -1

# bandage = [4, 2, 7]
# health = 20
# attacks = [[1, 15], [5, 16], [8, 6]]  # result = -1

bandage = [1, 1, 1]
health = 5
attacks = [[1, 2], [3, 2]]  # result = 3

print(solution(bandage, health, attacks))