# https://chaemi720.tistory.com/176

from sys import stdin

# RxC 격자판, T초 후 결과 구하기
R,C,T = map(int,stdin.readline().split())
dust = [list(map(int,stdin.readline().split())) for _ in range(R)]

# 공기청정기 위치
clean = []
for r in range(R):
    for c in range(C):
        if dust[r][c] == -1:
            clean.append([r,c])

# T초
for _ in range(T):
    # 동시에 확산을 위해
    room_dust = [[0] * C for _ in range(R)]
    # 1. 미세먼지 확산
    for r in range(R):
        for c in range(C):
            # 미세먼지가 있다면
            if dust[r][c] != 0 and dust[r][c] != -1:
                du = dust[r][c]//5
                if du:
                    # 4방향 미세먼지 확산
                    for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                        nr = r + dr
                        nc = c + dc
                        # 공기청정기가 아니면 확산 가능
                        if 0 <= nr < R and 0 <= nc < C and dust[nr][nc] != -1:
                            room_dust[nr][nc] += du
                            room_dust[r][c] -= du
    for i in range(R):
        for j in range(C):
            dust[i][j] += room_dust[i][j]
    print(dust)
    # 2. 공기청정기 돌리기
    # 위쪽 공기청정기(반시계방향)
    lr = [0,-1,0,1]
    lc = [1,0,-1,0]
    direction_l = 0
    previous_l = 0
    l_x,l_y = clean[0]
    while True:
        # 한 칸 씩 이동
        l_x += lr[direction_l]
        l_y += lc[direction_l]
        # 제자리로 돌아왔으면 멈추기
        if l_x == clean[0][0] and l_y == clean[0][1]:
            break
        # 공기청정기 작동
        if 0 <= l_x < R and 0 <= l_y < C:
            dust[l_x][l_y], previous_l = previous_l, dust[l_x][l_y]
        else:
            l_x -= lr[direction_l]
            l_y -= lc[direction_l]
            direction_l += 1

    # 아래쪽 공기청정기(시계방향)
    rr = [0,1,0,-1]
    rc = [1,0,-1,0]
    direction_r = 0
    previous_r = 0
    r_x, r_y = clean[1]
    while True:
        # 한 칸 씩 이동
        r_x += rr[direction_r]
        r_y += rc[direction_r]
        # 제자리로 돌아왔으면 멈추기
        if r_x == clean[1][0] and r_y == clean[1][1]:
            break
        # 공기청정기 작동
        if 0 <= r_x < R and 0 <= r_y < C:
            dust[r_x][r_y], previous_r = previous_r, dust[r_x][r_y]
        else:
            r_x -= rr[direction_r]
            r_y -= rc[direction_r]
            direction_r += 1

# 미세먼지 양 출력
dust_cnt = 0
for r in range(R):
    dust_cnt += sum(dust[r])

# 공기청정기가 -1로 표시되어있으므로
print(dust_cnt+2)