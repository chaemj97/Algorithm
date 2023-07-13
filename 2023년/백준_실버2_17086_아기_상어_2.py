'''
    접근법
        bfs를 이용하여 상어와의 최소 거리 구하기
    
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 상어 위치
que = deque()
for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            que.append((r,c))
            
while que:
    cr,cc = que.popleft()
    for dr,dc in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
        nr = cr+dr
        nc = cc+dc
        if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 0:
            arr[nr][nc] = arr[cr][cc] + 1
            que.append((nr,nc))

answer = 0
for i in range(n):
    answer = max(answer,max(arr[i]))
print(answer-1)