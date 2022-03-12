n, m = map(int, input().split()) # 딕셔너리 구조를 이용한 문제
team_member, member_team = {}, {} 
for _ in range(n):
    team_name, member_number = input(), int(input()) # 걸그룹이름, 걸그룹 인원수
    team_member[team_name] = []
    for _ in range(member_number): # 걸그룹 인원수만큼 구성원 이름받기
        name = input()
        team_member[team_name].append(name) # {걸그룹 이름: [구성원 a, b, c, ...]}
        member_team[name] = team_name # {구성원 이름: 걸그룹 이름} 

for _ in range(m):
    name = input()
    problem = int(input())
    if problem == 0:
        for member in sorted(team_member[name]):
            print(member)
    else:
        print(member_team[name])