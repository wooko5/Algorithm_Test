# 몰랐던 점: 문자 슬리이싱, 덱구조, R과 D를 단순히 할 때 마다 구현하지 않는 것

T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    p = input() # 수행할 함수 ex) RDD
    n = int(input()) # 배열의 길이
    deque = input()[1:-1].split(',') # [과 ]을 배제하고 ','을 없애기 위한 문자열 슬라이싱

    count_R, front, rear = 0, 0, 0 # 'R'의 개수, 앞에서 버려야할 원소 개수, 뒤에서 버려야할 원소 개수
    for i in p:
        if i == 'R': # 배열을 거꾸로
            count_R += 1
        elif i == 'D': # 가장 첫번째 요소 삭제
            if count_R % 2 == 0: # 'R'의 개수가 짝수로 나왔다면 -> 굳이 안 바꿔도 됨 -> 앞에서부터 삭제
                front += 1
            else: # 'R'의 개수가 홀수로 나왔다면 -> 1번만 바꾸면 됨 -> 뒤에서부터 삭제
                rear += 1
            
    if front + rear <= n:
        deque = deque[front:n-rear] # f에서 부터 (n-b-1) 인덱스까지 부분 배열이식
        if count_R % 2 == 1: # 뒤집어서 출력
            print('['+','.join(deque[::-1])+']')
        else: # 그대로 출력
            print('['+','.join(deque)+']')
    else: # 삭제하는 요소가 배열의 길이보다 큰 경우 -> 당연히 오류!!
        print('error')