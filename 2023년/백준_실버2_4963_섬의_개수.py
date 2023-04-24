'''
    접근법 1
        BFS를 활용해 8방향 확인

'''
from collections import deque
import sys
input = sys.stdin.readline

while True:
    # 지도의 너비, 높이
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    # 지도
    arr = [list(map(int,input().split())) for _ in range(h)]
    island = 0
    
    que = deque()
    visited = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1 and visited[r][c] == 0:
                island += 1
                que.append((r,c))
                visited[r][c] = island
                while que:
                    # 현 위치
                    cr,cc = que.popleft()
                    # 연결 확인 8방향
                    for dr,dc in [[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]]:
                        nr,nc = cr+dr,cc+dc
                        # 범위 내 확인한 적 없고 땅
                        if 0<=nr<h and 0<=nc<w and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                            visited[nr][nc] = island
                            que.append((nr,nc))
    print(island)