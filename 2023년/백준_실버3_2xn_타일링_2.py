'''
    접근법 1
        규칙
            A(1) = 1
            A(2) = 3
            A(3) = 5
            A(4) = 11
            A(n) = A(n-1) + A(n-2)*2
        -> dp
'''

import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(1001)
dp[1] = 1
dp[2] = 3
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2)%10007

print(dp[n])