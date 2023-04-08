'''
    접근법 1
        규칙 A(n) = A(n-3) + A(n-2) (n > 3)
        -> dp

'''

import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n = int(input())
    dp = [0]*(101)
    dp[1],dp[2],dp[3] = 1,1,1
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[n])