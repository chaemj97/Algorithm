'''
    접근법 
    
'''

import sys
input = sys.stdin.readline

# 보드의 세로, 가로
n, m = map(int,input().split())
board = [input().split() for _ in range(n)]

red = []
blue = []
goal = []
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            red.append([r,c])
        elif board[r][c] == 'B':
            blue.append([r,c])
        elif board[r][c] == 'O':
            goal.append([r,c])
            
