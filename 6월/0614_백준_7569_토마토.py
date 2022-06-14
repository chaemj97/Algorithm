from collections import deque
from sys import stdin

# 토마토 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
# 가로 M, 세로 N, 높이 H
M,N,H = map(int,stdin.readline().split())

tomato = [[list(map(int,stdin.readline().rstrip().split())) for _ in range(N)] for __ in range(H)]

# 익은 토마토 위치
ripetomato = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 1:
                ripetomato.append([h,r,c])

# 토마토 익히기
while ripetomato:
    ch,cr,cc = ripetomato.popleft()
    # 우,하,좌,상,위,아래
    for dh,dr,dc in [(0,0,1),(0,1,0),(0,0,-1),(0,-1,0),(1,0,0),(-1,0,0)]:
        nh = ch + dh
        nr = cr + dr
        nc = cc + dc
        # 상자 안에 있고 안 익은 토마토 -> 익히기
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and tomato[nh][nr][nc] == 0:
            tomato[nh][nr][nc] = tomato[ch][cr][cc] + 1
            ripetomato.append([nh,nr,nc])

# 다 익었는가?
day = 0
for h in range(H):
    for r in range(N):
        day = max(day,max(tomato[h][r]))
        # 덜 익은 토마토 1개라도 있다면 실패
        if tomato[h][r].count(0):
            print(-1)
            exit(0)

# 익은 토마토 번호가 1로 시작해서
print(day-1)