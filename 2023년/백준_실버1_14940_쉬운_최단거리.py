'''
    접근법
        bfs를 활용하여 최단거리 구하기
    
'''
from collections import deque
import sys
input = sys.stdin.readline

# 지도의 크기
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
# 0은 갈 수 없는 땅 / 1은 갈 수 있는 땅 /2는 목표지점

answer = [[-1]*m for _ in range(n)]

que = deque()
for r in range(n):
    for c in range(m):
        # 목표 지점?
        if arr[r][c] == 2:
            que.append((r,c))
            answer[r][c] = 0
        # 벽
        elif arr[r][c] == 0:
            answer[r][c] = 0
            
while que:
    # 현 위치
    cr,cc = que.popleft()
    # 이동 : 가로, 세로
    for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
        nr = cr + dr
        nc = cc + dc
        # 범위 내 + 확인한 적 X
        if 0 <= nr < n and 0 <= nc < m and answer[nr][nc] == -1:
            # 갈 수 있는 땅
            if arr[nr][nc] == 1:
                answer[nr][nc] = answer[cr][cc] + 1
                que.append((nr,nc))

# 결과 출력
for i in range(n):
    print(*answer[i])