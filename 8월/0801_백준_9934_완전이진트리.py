from re import M
from sys import stdin
input = stdin.readline

# 트리 깊이
K = int(input())
# 방문한 빌딩의 번호
building = list(map(int,input().split()))
tree = [[] for _ in range(K)]

def Maketree(arr,level):
    # 중위 순회니 arr의 중심값의 깊이가 level 
    mid = len(arr)//2
    tree[level].append(arr[mid])
    # 1개 있으면 끝
    if len(arr) == 1:
        return
    # 왼쪽 자식들
    Maketree(arr[:mid],level+1)
    # 오른쪽 자식들
    Maketree(arr[mid+1:],level+1)

Maketree(building,0)

# 각 레벨에 있는 빌딩 번호 출력
for i in range(K):
    print(*tree[i])

