'''
    접근법 
        n = 1 -> 1
        n = 2 -> 10
        n = 3 -> 100
                 101
        n = 4 -> 1000
                 1001
                 1010
        n = 5 -> 10'000'
                 10'001'
                 10'010'
                 10'100'
                 10'101'
        
        dp[n] = dp[n-2] + dp[n-1]
    
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*91
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])