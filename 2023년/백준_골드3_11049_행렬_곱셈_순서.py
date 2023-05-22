'''
    접근법
    
'''

import sys
input = sys.stdin.readline

# 행렬의 수
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

# i : 
for i in range(1,n):
    for j in range(0,n-i):
        # 차이가 1칸
        if i == 1:
            dp[j][j+i] = matrix[j][0]*matrix[j][1]*matrix[j+i][1]
            continue
        
        # 차이가 2칸 이상
        dp[j][j+i] = 2**32 # 최댓값
        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i],
                             dp[j][k]*dp[k+1][j*i])