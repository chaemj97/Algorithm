# 빨간 구슬만 빼내기
# . : 빈칸, # : 장애물/벽, O : 구멍, R : 빨간 구슬, B : 파란 구슬

# 보드의 세로, 가로
N,M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 1. 구슬/구멍 위치 찾기
for r in range(1,N-1):
    for c in range(1,M-1):
        if board[r][c] == 'R':
            rr,rc = r,c
        elif board[r][c] == 'B':
            br,bc = r,c
        elif board[r][c] == 'O':
            hr,hc = r,c



def dfs():
    d = [[0,-1],[1,0],[0,1],[-1,0]]
    visited = {}
    visited[(rr,rc)] = 1

    
