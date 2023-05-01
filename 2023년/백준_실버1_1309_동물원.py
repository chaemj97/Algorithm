'''
    접근법 1
        n = 1 -> answer = 3
        n = 2 -> answer = 7
        
        i번째 줄에 사자가 없는 경우 -> i+1번째 줄에 3가지
        i번째 줄에 사자가 있는 경우 -> i+1번째 줄에 빈 우리 혹은 반대방향인 총 2가지
        
        dp[i] = dp[i-2]*3 + (dp[i-1]-dp[i-2])*2
              = dp[i-2] + dp[i-1]*2

'''

import sys
input = sys.stdin.readline

N = int(input())

dp = [1,3]+[0]*(N-1)
for i in range(2,N+1):
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901
    
print(dp[N])
