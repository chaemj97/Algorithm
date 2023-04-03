'''
    접근법 1
        https://chaemi720.tistory.com/282

'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

# inorder의 값 index 리스트
inorder_index = [0]*(n+1)
for i in range(n):
    inorder_index[inorder[i]] = i

# inorder의 시작 인덱스, 끝 인덱스/postorder의 시작 인덱스, 끝 인덱스
def preorder(in_l,in_r,post_l,post_r):
    global inorder,postorder
    # 재귀 종료 조건
    if in_l > in_r or post_l > post_r:
        return
    
    # 현 트리에서 최상위 루트
    root = postorder[post_r]
    print(root,end=' ')

    # inorder에서 root 위치 찾기
    in_root = inorder_index[root]
    # 왼쪽 서브트리
    # 왼쪽 서브트리 노드의 개수
    left = in_root - in_l
    preorder(in_l, in_root-1, post_l, post_l+left-1)
    # 오른쪽 서브트리
    # 오른쪽 서브트리 노드의 개수
    right = in_r - in_root
    preorder(in_root+1,in_r,post_r-right,post_r-1)

preorder(0,n-1,0,n-1)