# https://www.acmicpc.net/problem/2638

from collections import deque

# 세로, 가로
N, M = map(int,input().split())
# 모눈 종이
arr = [list(map(int,input().split())) for _ in range(N)]

# 치즈의 개수
cheese = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            cheese += 1

# 치즈 겉 녹이기
def mel():
    # 겉의 공간만 담을 수 있음
    q = deque()
    q.append([0,0])
    # 방문 표시
    check = [[-1]*M for _ in range(N)]
    check[0][0] = 0
    while q:
        cr,cc = q.popleft()
        for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            nr = cr + dr
            nc = cc + dc
            # 범위 내, 방문한 적 없
            if 0 <= nr < N and 0 <= nc < M and check[nr][nc] == -1:
                # 빈공간
                if arr[nr][nc] == 0:
                    q.append([nr,nc])
                    check[nr][nc] = 0
                # 치즈
                else:
                    arr[nr][nc] += 1

# 녹는데 걸리는 총 시간
time = 0
while cheese:
    mel()
    time += 1
    for i in range(N):
        for j in range(M):
            # 공기와 2변 이상 접한 치즈
            if arr[i][j] >= 3:
                arr[i][j] = 0
                cheese -= 1
            # 공기와 1변 접한 치즈
            elif arr[i][j] == 2:
                arr[i][j] = 1

print(time)