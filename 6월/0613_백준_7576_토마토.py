from sys import stdin
from collections import deque

# 상자 크기 M*N
M,N = map(int,stdin.readline().split())
tomato = [list(map(int,stdin.readline().split())) for _ in range(N)]

# 익은 토마토 위치
ripetomato = deque()
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            ripetomato.append((r,c))

# 익은 토마토 주변 토마토 익히기
while ripetomato:
    cr,cc = ripetomato.popleft()
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = cr + dr
        nc = cc + dc
        if 0 <= nr < N and 0 <= nc < M and tomato[nr][nc] == 0:
            tomato[nr][nc] = tomato[cr][cc] + 1
            ripetomato.append((nr,nc))

# 걸린 날
day = 0

# 다 익었는가 확인해보자
for i in tomato:
    day = max(day,max(i))
    # 익지 않은 토마토가 있다면 실패
    if i.count(0):
        day = 0
        break

# 익은 토마토 번호가 1이라서
print(day-1)