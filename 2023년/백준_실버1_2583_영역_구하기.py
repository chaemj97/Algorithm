'''
    접근법
        1. 직사각형 위치 표시
        2. 빈 칸 찾아 그 빈 칸의 영역 넓이 구하기
'''
from collections import deque
import sys
input = sys.stdin.readline

# MxN 크기의 모눈 종이 위에 K개의 직사각형
m,n,k = map(int,input().split())
arr = [[0]*m for _ in range(n)]

# 직사각형 위치 표시
for _ in range(k):
    r1,c1,r2,c2 = map(int,input().split())
    for r in range(r1,r2):
        for c in range(c1,c2):
            arr[r][c] = 1

# from pprint import pprint
# pprint(arr)

# 분리된 영역 구하기

# 분리된 영역 넓이
def bfs(r,c):
    area = 1
    que = deque()
    que.append([r,c])
    arr[r][c] = 2
    while que:
        cr,cc = que.popleft()
        for dr,dc in [[1,0],[0,1],[0,-1],[-1,0]]:
            nr = cr + dr
            nc = cc + dc
            # 영역 내 빈칸?
            if 0<= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                area += 1
                que.append([nr,nc])
                arr[nr][nc] = 2
    return area

cnt = 0
areas = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt += 1
            area = bfs(i,j)
            areas.append(area)
print(cnt)
print(*sorted(areas))