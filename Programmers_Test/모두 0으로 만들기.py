"""
a의 길이가 2 이상 300,000 이하라서 재귀의 최대치를 '30만'으로 지정합니다
2021.11.18 프로그래머스 레벨 3, 월간 코드 챌린지 시즌2
"""
import sys
sys.setrecursionlimit(300000)

def dfs(node, a, matrix, visited):
    global answer
    current = a[node]
    visited[node] = True

    for i in matrix[node]: # 반복을 이용한 
        if visited[i] == False:
            current += dfs(i, a, matrix, visited)
    answer += abs(current)
    return current


def solution(a, edges):
    if sum(a) != 0: # a 가중치의 전체 합이 0이라면 가중치를 0으로 만드는 것이 가능하기에 
        return -1 # a 가중치 전체 합이 0이 아니라면 0으로 만드는 것이 불가능하다
    
    global answer
    answer = 0
    matrix = [[] for _ in range(len(a))]
    
    for i, j in edges:
        matrix[i].append(j)
        matrix[j].append(i)

    visited = [False] * len(a)
    dfs(0, a, matrix, visited)
    return answer