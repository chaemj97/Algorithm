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
node = [0]*(10000)
node[1] = 'A'

for _ in range(N):
    # 루트, 자식, 자식
    a,b,c = input().split()
    i = node.index(a)
    if b != '.':
        node[i*2] = b
    if c != '.':
        node[i*2+1] = c

# 전위순회
def preorder(idx):
    if node[idx]:
        print(node[idx],end='')
        preorder(idx*2)
        preorder(idx*2+1)
preorder(1)
print()

# 중위순회
def inorder(idx):
    if node[idx]:
        inorder(idx*2)
        print(node[idx],end='')
        inorder(idx*2+1)
inorder(1)
print()

# 후위순회
def postorder(idx):
    if node[idx]:
        postorder(idx*2)
        postorder(idx*2+1)
        print(node[idx],end='')
postorder(1)