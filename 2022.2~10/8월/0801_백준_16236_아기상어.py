from dis import dis
from sys import stdin
from collections import deque
input = stdin.readline

# 공간의 크기
N = int(input())

# 공간의 상태
space = [list(map(int,input().split())) for _ in range(N)]

# 아기 상어 위치 찾기
def wherebaby(space):
    for x in range(N):
        for y in range(N):
            if space[x][y] == 9:
                return x, y

# 1. 현재 아기상어 위치에 0으로 바꾸기
x, y = wherebaby(space)
space[x][y] = 0

babyShark = 2

# 먹을 수 있는 1번 물고기 찾기
def find(r,c,babyShark):
    # 방문 표시
    checked = [[0]*N for _ in range(N)]
    checked[r][c] = 1
    # (r,c,거리)
    que = deque()
    que.append((r,c,0))
    # 잡은 물고기
    fish = []
    while que:
        # 현 위치
        cr,cc,d = que.popleft()
        # 이동
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            nr = cr + dr
            nc = cc + dc
            # 범위 내에 있고 확인한 적 없다면
            if 0 <= nr < N and 0<= nc < N and checked[nr][nc] == 0:
                checked[nr][nc] = 1
                # 먹을 수 있는 물고기 == 상어보다 작은 물고기
                if 0 < space[nr][nc] < babyShark:
                    # 위치와 물고기까지 거리
                    fish.append((d+1,nr,nc))
                    que.append((nr,nc,d+1))
                # 빈 공간, 아기상어와 크기 같음 : 이동만 가능
                elif space[nr][nc] == 0 or space[nr][nc] == babyShark:
                    que.append((nr,nc,d+1))
    # 가장 가까운 물고기 구하기 + 왼쪽 위
    fish.sort()
    if fish:
        return [fish[0][0], fish[0][1], fish[0][2]]
    else:
        return []

eatCnt = 0
# 크기 작으면 먹을 수 있음

distance = 0
# 먹어보자
while True:
    fish = find(x,y,babyShark)
    # 먹을 수 있는 물고기 있는가?
    if fish:
        move, a, b = fish
        # 먹기
        space[a][b] = 0
        eatCnt += 1
        distance += move
        # 아기상어 크기 만큼 먹으면 크기 +1
        if eatCnt == babyShark:
            babyShark += 1
            eatCnt = 0
        # 아기상어 이동
        x,y = a,b
    else:
        break

print(distance)