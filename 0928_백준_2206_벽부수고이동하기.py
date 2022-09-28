import sys
from collections import deque
input = sys.stdin.readline

# NxM 행렬
N, M = map(int,input().split())

# 맵 (1:벽, 0:이동, 벽 1개 부셔도됨)
matrix = [list(map(int,input()[:-1])) for _ in range(N)]

# 방문 여부 + 벽 깬 여부
# visited[][][0] : 벽 부수기 전, visited[][][1] : 벽 부순 후
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
# 시작점
visited[0][0][0] = 1

# 현위치 (r,c), 벽 부순 횟수 cnt
def solve(r,c,cnt):
    que = deque()
    que.append((r,c,cnt))

    while que:
        # 현 위치
        cr,cc,break_cnt = que.popleft()
        # 도착?
        if cr == N-1 and cc == M-1:
            return visited[cr][cc][break_cnt]
        # 이동
        for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = cr + dr
            nc = cc + dc
            # 범위 내
            if 0 <= nr < N and 0 <= nc < M:
                # 벽X, 방문X
                if matrix[nr][nc] == 0 and visited[nr][nc][break_cnt] == 0:
                    # 이동하고 방문 표시
                    visited[nr][nc][break_cnt] = visited[cr][cc][break_cnt] + 1
                    que.append((nr,nc,break_cnt))
                # 벽O, 부순적X
                elif matrix[nr][nc] == 1 and break_cnt == 0:
                    # 벽 부수고 방문 표시
                    visited[nr][nc][1] = visited[cr][cc][0] + 1
                    que.append((nr,nc,1))
    # 도착하지 못했다.
    return -1

print(solve(0,0,0))