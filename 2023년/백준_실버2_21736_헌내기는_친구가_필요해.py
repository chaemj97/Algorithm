'''
    접근법
        bfs로 그래프 탐색
    
'''
from collections import deque
import sys
input = sys.stdin.readline

# 캠퍼스 크기
n,m = map(int,input().split())
# O는 빈 공간, X는 벽, I는 도연이, P는 사람
campus = [list(input().rstrip()) for _ in range(n)]

# 도연
Do = deque()
def find_Do():
    for r in range(n):
        for c in range(m):
            if campus[r][c] == 'I':
                Do.append([r,c])
                return

find_Do()
        
answer = 0
# 확인 여부
visited = [[0]*m for _ in range(n)]
while Do:
    # 도연이 현 위치
    cr,cc = Do.popleft()
    # 이동
    for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
        nr = cr + dr
        nc = cc + dc
        # 학교 내, 방문한 적 없는 곳
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
            # 빈 공간
            if campus[nr][nc] == 'O':
                visited[nr][nc] = 1
                Do.append((nr,nc))
            # 사람
            elif campus[nr][nc] == 'P':
                answer += 1
                visited[nr][nc] = 1
                Do.append((nr,nc))
                
if answer:
    print(answer)
else:
    print('TT')