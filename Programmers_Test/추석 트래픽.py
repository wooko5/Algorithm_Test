"""
주어진 데이터를 파싱해서 원하는 데이터로 만들어서 start_time, end_time을 알아내는 것은 쉬웠으나
float로 하면서 문제가 좀 꼬이기 시작했고, 결국 int로 바꾸는 방법을 인터넷에서 코드를 보고 알아냈다.
접근은 쉬었으나 푸는 사람 입장에서 좀더 간단하게 int로 접근했어야했다.
카카오 문제는 좀 더 생각하고 꼼꼼하게 풀어야겠다
프로그래머스 레벨3, 카카오 블라인드 구현문제
2021.11.10
"""
def check(time, array):
    count = 0
    start = time
    end = time + 1000 # 1초에 1000을 곱해서 1000이다
    for arr in array:
        if arr[1] >= start and arr[0] < end:
            count += 1
    return count


def solution(lines):
    array = []
    if len(lines) == 1:
        return 1
    answer = 0
    
    for line in lines:
        year, date, time = line.split()
        date = date.split(':')
        time = float(time.replace('s', ''))*1000
        end = (int(date[0])*3600 + int(date[1])*60 + float(date[2]))*1000
        start = end - time + 1 # 모든 숫자가 1000을 곱하기에 0.001에 1000을 곱한 것을 의미한다 
        array.append([start, end]) # 0.001이 나온 이유는 3자리수까지만 시간을 치기 때문에 end - time을 하면 0.001을 더해줘야한다
    
    for arr in array:
        answer = max(answer, check(arr[0], array), check(arr[1], array))
    return answer