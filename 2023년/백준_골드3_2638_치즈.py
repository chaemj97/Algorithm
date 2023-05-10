'''
    접근법
        bfs
        공백 상하좌우 확인하기
            공백 근처에 치즈가 있으면 그 치즈는 공기접촉 횟수 +1
    
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
# 1 : 치즈, 0 : 공백
cheese = [list(map(int,input().split())) for _ in range(n)]

# 치즈 수
cnt = 0
for i in range(n):
    cnt += cheese[i].count(1)
    
# 치즈 녹이기
def mel():
    que = deque()
    # 모눈종이 가장자리는 치즈X
    # 공백의 4방향 확인
    que.append([0,0])
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 0
    while que:
        cr,cc = que.popleft()
        for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = cr + dr
            nc = cc + dc
            # 범위 내, 방문한 적 없는
            if 0<=nr<n and 0<=nc<m and visited[nr][nc] == -1:
                # 빈공간?
                if cheese[nr][nc] == 0:
                    visited[nr][nc] = 0
                    que.append([nr,nc])
                # 치즈? -> 공기와 접촉했다
                else:
                    # 접촉 횟수 +1
                    cheese[nr][nc] += 1
                    
# 녹는데 걸리는 총 시간
time = 0
while cnt > 0:
    time += 1
    # 치즈 녹이기
    mel()
    # 2변 이상 공기와 접촉 찾기
    for r in range(n):
        for c in range(m):
            # 2변 이상 공기와 접촉
            if cheese[r][c] >= 3:
                cnt -= 1
                cheese[r][c] = 0
            # 1변만 공기와 접촉
            elif cheese[r][c] == 2:
                cheese[r][c] = 1

print(time)
                