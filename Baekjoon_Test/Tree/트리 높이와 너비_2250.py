# 중위 순회를 이용하면 x축을 기준으로 왼쪽부터 방문한다는 특징이 있다
# 이 문제는 중위 순회 알고리즘을 이용하고, 추가적으로 Level 값을 저장하도록 해서 문제를 해결할 수 있다
class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1 # 이 숫자를 통해 부모노드를 확인해서 루트노드인지 아닌지 확인한다, 즉 부모노드가 없는 노드가 루트노드임
        self.number = number
        self.left_node = left_node
        self.right_node = right_node
    
def inorder(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        inorder(tree[node.left_node], level+1)
    level_min[level] = min(level_min[level], x) # 해당 높이(level)에서 가장 왼쪽(최소값)에 있는 변수찾기
    level_max[level] = max(level_max[level], x) # 해당 높이(level)에서 가장 오른쪽(최대값)에 있는 변수찾기
    x += 1
    if node.right_node != -1:
        inorder(tree[node.right_node], level+1)

n = int(input())
tree = {}
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1

for i in range(1, n+1): # 트리 초기화하기
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n): # 트리에 숫자 삽입하기
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node

    if left_node != -1: # 루트노드가 아니라면
        tree[left_node].parent = number # 부모가 어떤 노드인지 알기위해 기록해두기
    if right_node != -1: # 루트노드가 아니라면
        tree[right_node].parent = number # 부모가 어떤 노드인지 알기위해 기록해두기

for i in range(1, n+1):
    if tree[i].parent == -1: # 부모가 없는 노드를
        root = i # 루트노드라고 생각하기

inorder(tree[root], 1) # 루트노드에서부터 중위 순회를 하기

answer_level = 1
answer_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1): # 
    width = level_max[i] - level_min[i] + 1 # 같은 레벨의 노드를 모두 순회하면서 너비값 구하기
    if answer_width < width:
        answer_level = i # 높이(level)를 기록
        answer_width = width # 가장 넓은 너비를 기록하기

print(answer_level, answer_width)