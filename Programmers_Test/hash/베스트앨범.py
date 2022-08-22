"""
프로그래머스 고득점 kit, Hash편
play_list 라는 배열을 이용해서 [장르, 재생횟수, 고유번호(index)]를 생성하고, 장르는 오름차순, 재생횟수는 역정렬로 해준다.
music 이라는 해시(딕셔너리)를 이용해서 음악 장르마다 총 재생횟수를 구해서 역정렬을 해준다.
총 재생횟수가 많은 장르인 음악을 먼저 뽑되, 고유번호를 2개씩 뽑은 정답 배열을 반환하면 된다
2021.10.04
"""

def solution(genres, plays):
    answer = []
    play_list = []
    music = dict()
    
    for i in range(len(genres)):
        play_list.append([genres[i], plays[i], i])
    
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = plays[i]
        else:
            count = music[genres[i]]
            count += plays[i]
            music[genres[i]] = count
    
    play_list = sorted(play_list, key = lambda x: (x[0], -x[1]))
    music = sorted(music.items(), key = lambda x: -x[1]) # 리스트로 변환됨

    for genre in music:
        cnt = 0
        for i in range(len(play_list)):
            if genre[0] == play_list[i][0]: # 원하는 음악장르가 맞다면
                answer.append(play_list[i][2]) # 고유번호를 정답 배열에 추가
                cnt += 1
                if cnt == 2: # 같은 장르인 음악을 2개만 뽑기
                    break
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))