

from sys import stdin
input = stdin.readline

# 집의 크기
N = int(input())
# 집의 상태
home = [list(map(int,input().split())) for _ in range(N)]
result = 0

# shape : 가로, 세로, 대각선
def dfs(r,c,shape):
    global result
    # 도착?
    if r == N-1 and c == N-1:
        result += 1
        return
    # 오른쪽으로 이동 가능
    if shape == 0 or shape == 2:
        if c + 1 < N and home[r][c+1] == 0:
            dfs(r, c+1, 0)
    # 아래쪽으로 이동 가능
    if shape == 1 or shape == 2:
        if r + 1 < N and home[r+1][c] == 0:
            dfs(r+1,c,1)
    # 오른쪽 아래 대각선 방향으로 이동 가능
    # 대각선 방향은 3군데가 빈 곳이어야 함
    if r + 1 < N and c + 1 < N:
        if home[r][c+1] == 0 and home[r+1][c] == 0 and home[r+1][c+1] == 0:
            dfs(r+1,c+1,2)

dfs(0,1,0)
print(result)