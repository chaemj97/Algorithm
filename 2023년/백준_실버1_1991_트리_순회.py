'''
    접근법 1
        전위 순회 : (루트) (왼쪽 자식) (오른쪽 자식)
        중위 순회 : (왼쪽 자식) (루트) (오른쪽 자식)
        후위 순회 : (왼쪽 자식) (오른쪽 자식) (루트)
'''

import sys
input = sys.stdin.readline

# 노드의 개수
N = int(input())
# 트리
tree = {}
for _ in range(N):
    root,left,right = input().split()
    tree[root] = [left,right]

# 전위순회 : 루트 -> 왼쪽 -> 오른쪽
def preorder(root):
    if root != '.':
        # 루트
        print(root,end='')
        # 왼쪽
        preorder(tree[root][0])
        # 오른쪽
        preorder(tree[root][1])
preorder('A')
print()

# 중위순회 : 왼쪽 -> 루트 -> 오른쪽
def inorder(root):
    if root != '.':
        # 왼쪽
        inorder(tree[root][0])
        # 루트
        print(root,end='')
        # 오른쪽
        inorder(tree[root][1])
inorder('A')
print()

# 후위순회 : 왼쪽 -> 오른쪽 -> 루트
def postorder(root):
    if root != '.':
        # 왼쪽
        postorder(tree[root][0])
        # 오른쪽
        postorder(tree[root][1])
        # 루트
        print(root,end='')
postorder('A')