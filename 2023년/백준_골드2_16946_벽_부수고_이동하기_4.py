'''
    접근법
        각 벽마다 확인했더니 시간초과
        
        <구현>
        0의 묶음을 그룹으로 표시
            각 그룹당 몇개씩 있는지 확인
            
        각 벽의 상하좌우에 0의 그룹 확인 
'''
from collections import deque
import sys
input = sys.stdin.readline

''' 시간 초과
n,m = map(int,input().split())
# 0: 이동 가능, 1 :벽
arr = [list(input().rstrip()) for _ in range(n)]

def bfs(r,c):
    cnt = 0
    que = deque()
    que.append((r,c))
    visited = [[0]*m for _ in range(n)]
    visited[r][c] = 1
    while que:
        cr,cc = que.popleft()
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr = cr+dr
            nc = cc+dc
            if 0<=nr<n and 0<=nc<m and arr[nr][nc] == '0' and visited[nr][nc] == 0:
                cnt += 1
                visited[nr][nc] = 1
                que.append((nr,nc))
    return cnt

for r in range(n):
    for c in range(m):
        if arr[r][c] == '1':
            arr[r][c] = str(bfs(r,c)+1)

# 결과 출력
for r in range(n):
    print(''.join(arr[r]))
'''

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
g = 1
# 각 그룹마다 몇개씩 있는지 구하기
group = {0:0}
zero = [[0]*m for _ in range(n)]

def bfs(r,c):
    que = deque()
    que.append((r,c))
    cnt = 1
    while que:
        cr,cc = que.popleft()
        zero[cr][cc] = g
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr = cr+dr
            nc = cc+dc
            if 0<=nr<n and 0<=nc<m and graph[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append((nr,nc))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        # 0의 묶음을 그룹화
        if graph[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            group[g] = bfs(i,j)
            g += 1

# 벽을 부순 후 이동할 수 있는 칸의 수 세기
for i in range(n):
    for j in range(m):
        # 벽인가?
        if graph[i][j] == 1:
            zero_group = set()
            # 4방향에 0의 그룹 확인
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr = i + dr
                nc = j + dc
                if 0<=nr<n and 0<=nc<m:
                    zero_group.add(zero[nr][nc])

            # 0의 개수 세기
            for z in zero_group:
                graph[i][j] += group[z]
                graph[i][j] %= 10
                
# 결과 출력
for g in graph:
    print(''.join(map(str,g)))