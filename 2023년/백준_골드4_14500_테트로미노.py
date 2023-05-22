'''
    접근법 
        4방향 돌면서 재귀
        ㅗ 모양은 따로 확인
    
'''

import sys
input = sys.stdin.readline

# 세로, 가로
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# (r,c) : 현재 위치, cnt : 정사각형 수, s : 합, used : 사용한 정사각형 위치
def tetromino(r,c,cnt,s,used):
    global answer
    # 4개 다 사용
    if cnt == 4:
        answer = max(answer,s)
        return
    # 테트로미노 만들기 3방향(위, 아래, 오른쪽)
    for dr, dc in [[-1,0],[1,0],[0,1]]:
        nr = r + dr
        nc = c + dc
        # 종이 안에 있고, 사용한 적 없는 정사각형 
        if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in used:
            # ㅗ 모양은 만들 수 없다.
            tetromino(nr,nc,cnt+1,s+arr[nr][nc],used+[(nr,nc)])
            # ㅗ 모양 만들기
            if cnt == 3:
                past_r, past_c = used[1]
                for dr, dc in [[-1,0],[1,0],[0,1],[0,-1]]:
                    next_r = past_r + dr
                    next_c = past_c + dc
                    # 종이 안에 있고, 사용한 적 없는 정사각형
                    if 0 <= next_r < n and 0 <= next_c < m and (next_r,next_c) not in used:
                        tetromino(next_r,next_c,cnt+1,s+arr[next_r][next_c],used+[(next_r,next_c)])
answer = 0
for r in range(n):
    for c in range(m):
        # (r,c)에서 시작
        tetromino(r,c,1,arr[r][c],[(r,c)])
        
print(answer)