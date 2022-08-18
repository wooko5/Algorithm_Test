from collections import Counter
# collections의 Counter는 배열을 딕셔너리 구조(hash)로 바꿔주는 라이브러리 함수

def solution(participant, completion):
    participant.sort() # 정렬하는 이유: participant와 completion 모두 사전순으로 정렬해서 value를 빼기위함
    completion.sort()

    return list(Counter(participant) - Counter(completion))[0]

#print(Counter(participant))
#print(Counter(completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))