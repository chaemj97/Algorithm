'''
    접근법
    
'''

import sys
input = sys.stdin.readline

# 방의 크기
n,m = map(int,input().split())
# 처음 위치(r,c), 방향(d)
r,c,d = map(int,input().split())
if d%2:
    d = (d+2)%2
# 반시계 방향
direction = [[-1,0],[0,-1],[1,0],[0,1]]*2
room = [list(map(int,input().split())) for _ in range(n)]

answer = 0

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
    if room[r][c] == 0:
        answer += 1
        room[r][c] = 1
    
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for dr,dc in direction[d+1:d+5]:
        nr = r+dr
        nc = c+dc
        d = (d+1)%4
        if 0<=nr<n and 0<=nc<m and room[nr][nc] == 0:
            # 반시계 방향으로 90도 회전
            # 한 칸 전진
            r = nr
            c = nc
            break
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        # 후진이 가능하면 1칸 후진
        back_d = (d+2)%4
        back_r = r + direction[back_d][0]
        back_c = c + direction[back_d][1]
        if 0<=back_r<n and 0<=back_c<m:
            r = back_r
            c = back_c
        # 후진이 안된다면 작동 멈추기
        else:
            break
print(answer)