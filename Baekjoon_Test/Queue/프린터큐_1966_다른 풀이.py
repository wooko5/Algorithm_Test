"""
https://dndi117.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1966%EB%B2%88-%ED%94%84%EB%A6%B0%ED%84%B0-%ED%81%90-%ED%81%90%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%92%80%EC%9D%B4
일반적인 큐 문제에 중요도라는 개념을 더해서 조금 복잡해졌다. 특히 중요도가 중복될 수 있기 때문에 주의가 필요하다. 
예시에서처럼 중요도로 1,1,9,1,1,1이 들어오면 '중요도가 1인 문서의 출력 순서'를 구하는 방법은 통하지 않기 때문이다 
나는 입력받은 큐를 que, 인덱스를 원소로 넣은 idx_que를 이용하여 풀었다.
que에 대한 푸시, 팝을 동일하게 idx_que에 적용하면 한 문서가 출력됐을 때(pop됐을 때)의 인덱스를 알 수 있기 때문이다 
그리고 백준 사이트의 큐, 스택 문제들은 리스트를 이용하여 풀 때 시간 초과가 자주 나오므로 deque 라이브러리를 이용하여 풀었다

1. que 로 문서의 중요도를 입력받는다 
2. idx_que에 인덱스를 입력해준다 
3. 큐의 첫 번째 요소가 큐의 최대값이라면 pop해준다. idx_que도 pop해준다
4. pop할 때마다 cnt로 몇 번째로 인쇄된 것인지를 카운트해준다 
5. 큐의 첫 번째 요소가 큐의 최대값이 아니라면 pop한 후 push해서 큐의 마지막으로 보내준다. idx_que에 대해서도 동일하게 처리한다 
6. idx_que에서 pop한 요소가 x(인쇄 순번을 구하는 문서)와 같다면 cnt를 출력해준다
"""
test_case = int(input()) 
for _ in range(test_case): # 테스트 케이스만큼 반복
    n , target = map(int,input().split()) # 배열의 크기(여기서 사용x), 목표 원소
    queue = list(map(int,input().split())) # 문서의 중요도 위한 큐 생성
    index_queue = list(range(n)) # 큐의 원소들에 대한 index 큐 생성
    count = 0 

    while queue: # 큐에 원소가 없을 때까지 반복
        if queue[0] == max(queue): # 큐의 가장 앞의 원소가 현재 큐의 최대값이라면 
            count += 1 # count를 +1 해주고
            queue.pop(0) # 가장 앞의 원소를 버린다 
            if index_queue.pop(0) == target: # 큐의 가장 앞의 원소가 현재 큐의 최대값이고, index 큐에서 목적 원소라면
                print(count) # 지금까지의 count 출력 
        else:
            queue.append(queue.pop(0)) # 큐의 원소를 마지막에 붙인다
            index_queue.append(index_queue.pop(0)) # index 큐의 원소를 마지막에 붙인다