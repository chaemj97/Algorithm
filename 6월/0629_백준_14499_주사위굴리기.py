

from sys import stdin
import copy
input = stdin.readline

# 지도의 세로,가로 / 주사위를 놓은 곳의 좌표 / 명령의 개수 
N, M, x, y, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
# 1234 -> 동서북남
orders = list(map(int,input().split()))
move = [[0,0],[0,1],[0,-1],[-1,0],[1,0]]

# [북, 위, 남, 아래, 동, 서]
dice = [0]*6

move_idx = [
    [],
    # 동
    [0,5,2,4,1,3],
    # 서
    [0,4,2,5,3,1],
    # 북
    [1,2,3,0,4,5],
    # 남
    [3,0,1,2,4,5]
]

# 명령
for order in orders:
    # 이동
    x, y = x + move[order][0], y + move[order][1]
    
    # 지도 바깥으로 이동은 무시
    if not (0 <= x < N) or not (0 <= y < M):
        x, y = x - move[order][0], y - move[order][1]
        continue

    # 굴리기
    a = copy.deepcopy(dice)
    for idx in range(6):
        dice[idx] = a[move_idx[order][idx]]

    # 이동한 칸에 값이 0이면 -> 주사위 바닥면에 쓰인 값 적기
    if board[x][y] == 0:
        board[x][y] = dice[3]
    # 0이 아니면 -> 칸에 쓰인 값을 주사위 바닥에 복사 / 칸은 0
    else:
        dice[3] = board[x][y]
        board[x][y] = 0

    # 주사위 윗면에 쓰여 있는 수 출력
    print(dice[1])

