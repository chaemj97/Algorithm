'''
    접근법
        바이러스 중 m개 선택 후 활성화 -> 확산 -> 모두 다 확산 가능한지 확인
    
'''
from itertools import combinations
import copy
from collections import deque
import sys
input = sys.stdin.readline

# 연구소 크기, 놓을 수 있는 바이러스 개수
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

# 바이러스
virus = []
# 빈칸의 개수 
blank_cnt = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == 2:
            virus.append([r,c])
        elif arr[r][c] == 0:
            blank_cnt += 1
            
answer = 2500
# 바이러스 중 m개 활성화하기 -> 바이러스 확산
for c in combinations(virus,m):
    temp = copy.deepcopy(arr)
    que = deque()
    visited = [[-1]*n for _ in range(n)]
    # 바이러스 활성화
    for i,j in c:
        que.append([i,j])
        visited[i][j] = 0
        
    # 바이러스 확산
    infection_cnt = 0
    result = 0
    while que:
        # 현 위치
        cr,cc = que.popleft()
        
        # 4방향
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr = cr+dr
            nc = cc+dc
            # 범위 내 방문 X
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                # 빈 칸
                if temp[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] + 1
                    que.append([nr,nc])
                    infection_cnt += 1
                    result = max(result,visited[nr][nc])
                # 비활성 바이러스
                elif temp[nr][nc] == 2:
                    visited[nr][nc] = visited[cr][cc] + 1
                    que.append([nr,nc]) 
    
    if infection_cnt == blank_cnt:
        answer = min(answer,result)

if answer == 2500:
    print(-1)
else:
    print(answer)