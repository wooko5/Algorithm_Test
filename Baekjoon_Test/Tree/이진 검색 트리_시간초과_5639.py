"""
이렇게 만들면 
이진트리 만드는데 O(NlogN), 후위순회하는데 O(NlogN)이라서 시간초과가 난다
트리를 만들지 않고 바로 출력하는 방식을 택해야한다
"""

import sys; sys.setrecursionlimit(10**9)
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head
        
    def insert(self, value):
        self.current_node = self.head
        
        while True:
            if value < self.current_node.value:                   #기준 노드보다 input값이 작은 경우, 즉 왼쪽 자식 노드로 가야함
                if self.current_node.left != None:                #기준 노드의 왼쪽자식 노드에 값이 있는 경우, 즉 왼쪽 노드가 비어있지 않은 경우
                    self.current_node = self.current_node.left    #input값을 왼쪽 자식 노드 값으로 바꿔버린다
                else:                                             #기준 노드의 왼쪽자식 노드에 값이 없는 경우
                    self.current_node.left = Node(value)          #input값을 삽입한다
                    break
                    
            else:                                                #기준 노드보다 input값이 큰 경우, 즉 오른쪽 자식 노드로 가야함
                if self.current_node.right != None:              #기준 노드의 오른쪽자식 노드에 값이 있는 경우, 즉 오른쪽 노드가 비어있지 않은 경우
                    self.current_node = self.current_node.right  #input값을 오른쪽 자식 노드 값으로 바꿔버린다
                else:                                            #기준 노드의 오른쪽자식 노드에 값이 없는 경우
                    self.current_node.right = Node(value)        #input값을 삽입한다
                    break
    
    def search(self,value): #원하는 노드를 찾아주는 함수
        self.current_node = self.head
        
        while self.current_node:
            if self.current_node.value == value:           #현재 노드가 내가 찾고자하는 노드(value)인지 확인해보기
                return True
            elif value < self.current_node.value:          #찾고자하는 노드가 기준 현재 노드보다 작다면, 즉 왼쪽 자식노드로 가라
                self.current_node = self.current_node.left #만약에 찾고자하는 부분이 없다면 즉 None이면 while문을 빠져나올거임
            else:
                self.current_node = self.current_node.right
        return False
    
    def postOrder(self):
        def _postOrder(head):
            if head is None:
                pass
            else:
                _postOrder(head.left)
                _postOrder(head.right)
                print(head.value)
        _postOrder(self.head)

head = Node(int(input())) # 전위순회는 항상 제일 먼저 나온 키값이 루트 노드의 키값이다
BST = NodeMgmt(head) # 루트노드를 넣은 이진탐색트리 생성
count = 0
while count <= 10000:
    try:
        number = int(input())
    except:
        break
    BST.insert(number)
    count += 1
BST.postOrder() # 후위순회해서 출력