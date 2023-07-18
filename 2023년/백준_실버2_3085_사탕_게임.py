'''
    접근법
        1. 바꾸기 전 전체도 확인해야 함
        2. board[i][j]와 board[i+1][j]을 바꾸면 확인해야 하는 행/열
            i행, i+1행
        3. board[i][j]와 board[i][j+1]을 바꾸면 확인해야 하는 행/열
            j열, j+1열
        
        -> 바꿀때마다 전체 다 확인하기...
'''
import sys
input = sys.stdin.readline

# 보드의 크기
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

def check(i,j):
    global answer
    for i in range(n):
        # 행
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer,cnt)
        # 열
        cnt = 1
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer,cnt)
    
answer = 0
# 바꾸기
for i in range(n):
    for j in range(n):
        # 1. 행 범위
        if i + 1 < n:
            # 인접한 것끼리 바꾸기
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            # 먹을 수 있는 사탕 수 세기
            check(i,j)
            # 되돌리기
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
        # 2.열 범위
        if j + 1 < n:
            # 인접한 것끼리 바꾸기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check(i,j)
            # 되돌리기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

# 결과 출력
print(answer)