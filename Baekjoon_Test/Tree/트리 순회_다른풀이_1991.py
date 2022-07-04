# 이 방법을 선호하는 편
test_case = int(input()) # 전체 노드 개수(테스트 케이스 개수)
matrix = {} # 딕셔너리 구조

for _ in range(test_case):
    node, left_child, right_child = input().split()
    matrix[node] = [left_child, right_child]

def preorder(node): # 전위순회
    if node == '.':
        return
    print(node,end='')
    preorder(matrix[node][0])
    preorder(matrix[node][1])

def inorder(node): # 중위순회
    if node == '.':
        return
    inorder(matrix[node][0])
    print(node,end='')
    inorder(matrix[node][1])

def postorder(node): # 후위순회
    if node == '.':
        return
    postorder(matrix[node][0])
    postorder(matrix[node][1])
    print(node,end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
print('')
