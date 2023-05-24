'''
    접근법
        dp로 접근
    
'''

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n)]
dp[0] = [1]*10
for i in range(1,n):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][0:j+1])
        
print(sum(dp[n-1])%10007)
    