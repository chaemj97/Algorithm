'''
    접근법
        direction : 시계방향
        반시계 방향 (d+3)%4
        
        후진 : r - direction[d][0]
    
'''

import sys
input = sys.stdin.readline

# 방의 크기
n,m = map(int,input().split())
# 처음 위치(r,c), 방향(d)
r,c,d = map(int,input().split())
# 시계 방향
direction = [[-1,0],[0,1],[1,0],[0,-1]]
room = [list(map(int,input().split())) for _ in range(n)]
room[r][c] = 2
answer = 1

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소

    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for _ in range(4):
        # 반시계 방향 90도 회전
        d = (d+3)%4
        nr = r+direction[d][0]
        nc = c+direction[d][1]
        if 0<=nr<n and 0<=nc<m and room[nr][nc] == 0:
            # 청소
            room[nr][nc] = 2
            answer += 1
            # 한 칸 전진
            r = nr
            c = nc
            break
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        # 후진이 가능하면 1칸 후진
        back_r = r - direction[d][0]
        back_c = c - direction[d][1]
        if room[back_r][back_c] != 1:
            r = back_r
            c = back_c
        # 후진이 안된다면 작동 멈추기
        else:
            print(answer)
            break
