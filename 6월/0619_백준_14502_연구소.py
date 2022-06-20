# https://chaemi720.tistory.com/173

from copy import deepcopy
from sys import stdin
from collections import deque


# 지도 가로*세로 N*M
N, M = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for i in range(N)]

# 1. 벽 3개 만들기 -> 2. 바이러스 퍼트리기 
# -> 3. 안전 영역 크기 확인 -> 4. 최대면 갱신 -> 반복

max_safe_area = 0

# 바이러스 퍼트리기
def virus():
    global max_safe_area 
    # bfs
    # 바이러스 영역 표시
    deq = deque()
    # 복사해온 영역은 그대로 유지해야 하므로 deepcopy
    area = deepcopy(arr)
    for i in range(N):
        for j in range(M):
            # 바이러스면
            if arr[i][j] == 2:
                deq.append((i,j))
    
    # 2. 바이러스 퍼트리기
    while deq:
        # 현 위치
        cr,cc = deq.popleft()
        # 4방향 전염
        for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = cr + dr
            nc = cc + dc
            # 영역내에 있고 빈 칸이면 전염
            if 0 <= nr < N and 0 <= nc < M and area[nr][nc] == 0:
                area[nr][nc] = 2
                deq.append((nr,nc))
    
    safe_area = 0
    # 3. 안전 영역 크기 구하기
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                safe_area += 1
    
    # 4. 안전 영역 크기 최대면 갱신
    max_safe_area = max(max_safe_area,safe_area)

# 1. 벽 3개 만들기
def wall(cnt):
    # 벽 3개 설치?
    if cnt == 3:
        # 바이러스 터트리기
        virus()
        return
        
    # 벽 설치
    for i in range(N):
        for j in range(M):
            # 빈 칸이면 벽 세워도 됨
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                # 초기화
                arr[i][j] = 0

wall(0)
print(max_safe_area)