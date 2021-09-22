"""
인터넷을 참조했다
람다는 알고있었지만 n순위까지 정렬기준을 만드는게 가능한 것을 다시금 깨달았다
정말 쉬운 문제지만 너무 어렵게 접근한게 아닐까 싶다 
앞으로 문제를 더 풀어봐야겠따
2021.07.22
"""

"""
def solution(strings, n): # 직관적인 코드라 이것도 가져왔다
    strings = sorted(sorted(strings), key = lambda x : x[n]) # 사전순으로 정렬된 배열을 다시 우리가 원하는 순서로 정렬
    return strings
"""

def solution(strings, n):
    strings = sorted(strings, key = lambda x : (x[n], x.lower())) # 1순위 정렬 기준은 index, 2순위는 사전순
    return strings
    
strings = ["abce", "abcd", "cdx"]	
n = 2
print(solution(strings, n))