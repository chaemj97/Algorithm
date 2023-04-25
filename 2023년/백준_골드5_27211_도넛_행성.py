'''
    접근법 1
        목표 : 탐험할 수 있는 구역의 개수를 출력한다.
        
        bfs를 통해 구역번호별 탐방

'''
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
# 0 : 빈, 1 : 숲
arr = [list(map(int,input().split())) for _ in range(N)]

# 탐험
def bfs(r,c):
    que = deque()
    que.append((r,c))
    while que:
        cr,cc = que.popleft()
        # 이동
        for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
            # 한바퀴 도는 경우 생각하기!
            nr = (cr+dr)%N
            nc = (cc+dc)%M
            if arr[nr][nc] == 0:
                arr[nr][nc] = answer
                que.append((nr,nc))
            
# 구역의 개수
answer = 1
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            answer += 1
            bfs(r,c)
            
# 구역번호 2번부터 시작
print(answer-1)