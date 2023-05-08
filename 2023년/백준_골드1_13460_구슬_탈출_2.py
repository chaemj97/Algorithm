'''
    접근법
        visited : 4차원
        
        벽이나 구멍을 만날때 까지 이동
            파란 공이 구멍을 만나면 continue
            빨간 공이 구멍을 만나면 return
            빨간 공과 파란 공이 같은 위치에 존재하면 이동 횟수가 더 큰 공을 한 칸 뒤로 이동
    
'''
from collections import deque
import sys
input = sys.stdin.readline

# 보드의 세로, 가로
n, m = map(int,input().split())
board = [list(input()) for _ in range(n)]

# 빨간 구슬
rx,ry = -1,-1
# 파란 구슬
bx,by = -1,-1
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            rx,ry = r,c
        elif board[r][c] == 'B':
            bx,by = r,c

# 구슬 이동 후 다음 위치 (구멍에 빠지거나 벽에 부딪히거나)
def move(r,c,dr,dc):
    cnt = 0
    while True:
        cnt += 1
        r += dr
        c += dc
        # 이동 위치가 구멍인가?
        if board[r][c] == 'O':
            return r,c,cnt,True
        # 이동 위치가 벽인가?
        elif board[r][c] == '#':
            # 이동 직전 위치 return
            r -= dr
            c -= dc
            return r,c,cnt-1,False

def solution(rx,ry,bx,by):
    visited = [[[[-1]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # 방문 표시
    visited[rx][ry][bx][by] = 0
    que = deque([(rx,ry,bx,by)])
    while que:
        # 현재 빨간 구슬, 파란 구슬 위치
        crx,cry,cbx,cby = que.popleft()
        # 10번 이상 움직이면 pass
        if visited[crx][cry][cbx][cby] >= 10:
            continue
        
        # 4방향 이동
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            # 빨간 구슬 이동 후 위치(nrx,nry), 이동 횟수 (r_cnt), 구멍에 들어간 여부(r_goal)
            nrx,nry,r_cnt,r_goal = move(crx,cry,dr,dc)
            # 파란 구슬 이동
            nbx,nby,b_cnt,b_goal = move(cbx,cby,dr,dc)

            # 파란 구슬이 구멍에 빠지면 패스
            if b_goal:
                continue
            # 빨간 구슬이 구멍에 빠지면 끝
            if r_goal:
                return visited[crx][cry][cbx][cby] + 1
            
            # 빨간 구슬과 파란 구슬이 같은 위치에 있으면 안됨
            # 같은 위치로 나온다면 둘 중 이동 횟수가 큰 것을 한 칸 되돌리기
            if (nrx,nry) == (nbx,nby):
                if r_cnt > b_cnt:
                    nrx -= dr
                    nry -= dc
                else:
                    nbx -= dr
                    nby -= dc
  
            # 처음 방문하는가?
            if visited[nrx][nry][nbx][nby] == -1:
                visited[nrx][nry][nbx][nby] = visited[crx][cry][cbx][cby] +1
                que.append((nrx,nry,nbx,nby))
    return -1
                
print(solution(rx,ry,bx,by))