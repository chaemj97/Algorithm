'''
    접근법
        카메라 최대 8개
        각 카메라당 감시 가능한 영역 구하기
        각 카메라 감시 가능 영역 1개씩 선택 후 사각 지대 구하기
    
'''
from itertools import product
import sys
input = sys.stdin.readline

# 사무실 세로, 가로
n,m = map(int,input().split())
office = [list(map(int,input().split())) for _ in range(n)]

# [카메라 위치(r,c)와 종류 체크(num)]
camera = []
# CCTV 감시 할 구역
check_area_num = 0
for r in range(n):
    for c in range(m):
        if 1<= office[r][c] <= 5:
            camera.append([r,c,office[r][c]])
        elif office[r][c] == 0:
            check_area_num +=  1

# 감시
def watch(cam_direcion, r, c):
    # 감시한 구역 전체
    all_area = []
    for direction in cam_direcion:
        # 지금 방향으로 감시한 구역
        area = []
        for dr,dc in direction:
            # CCTV는 감시할 수 있는 방향에 있는 구역 전체를 감시
            move_r = r
            move_c = c
            while True:
                # 이동
                move_r += dr
                move_c += dc
                # 사무실내 + 벽이 아니다
                if 0<=move_r<n and 0<=move_c<m and office[move_r][move_c] != 6:
                    # 감시할 구역?
                    if office[move_r][move_c] == 0:
                        area.append([move_r,move_c])
                else:
                    break
        all_area.append(area)  
    return all_area


# 각 감시카메라의 관찰 방향
c1_d = [[[-1,0]],[[1,0]],[[0,-1]],[[0,1]]]
c2_d = [[[-1,0],[1,0]],[[0,-1],[0,1]]]
c3_d = [[[-1,0],[0,-1]], [[-1,0],[0,1]], [[1,0],[0,-1]], [[1,0],[0,1]]]
c4_d = [[[-1,0],[1,0],[0,-1]], [[-1,0],[1,0],[0,1]], [[-1,0],[0,-1],[0,1]],[[1,0],[0,-1],[0,1]]]
c5_d = [[[-1,0],[1,0],[0,-1],[0,1]]]

# 감시한 구역들 모으기
areas = []
# areas[i][j] : i번 카메라 j번째 감시 구역 
# ex) i번 카메라가 3번이면 0<= j < 4, i번 카메라가 5번이면 j = 0 
for cam in camera:
    r,c,num = cam
    if num == 1:
        areas.append(watch(c1_d,r,c))
    elif num == 2:
        areas.append(watch(c2_d,r,c))
    elif num == 3:
        areas.append(watch(c3_d,r,c))
    elif num == 4:
        areas.append(watch(c4_d,r,c))
    elif num == 5:
        areas.append(watch(c5_d,r,c))

# 감시할 구역은 최대 64 (가로 세로 최대가 8)
answer = 64
# 각 카메라에 감시구역 경우의 수 1개씩 뽑아서 사각지대 갯수 세기
# cartesian product
for a in product(*areas):
    # print(a)
    # -> ([0번째 카메라 감시 구역 list],[...])
    
    # 현재 감시 구역(중복 제외)
    watch = set()
    for i in a:
        # print(i)
        # -> [[r1,c1],[r2,c2]...]
        for r,c in i:
            watch.add((r,c))
    # 사각지대 구역 수 : 감시 가능 전체 구역 - 감시 구역
    blind_cnt = check_area_num - len(watch)
    answer = min(answer,blind_cnt)

# 결과
print(answer)
