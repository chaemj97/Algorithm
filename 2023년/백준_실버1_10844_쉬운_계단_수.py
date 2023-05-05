'''
    접근법 1
        0을 제외한 모든 숫자는 맨 앞에 올 수 있다.
        
        맨 뒤가 1이면 직전은 0
        맨 뒤가 9이면 직전은 8
        나머지는 각 2가지씩 있다.
'''

import sys
input = sys.stdin.readline

n = int(input())
# dp[자리수][맨 뒤에 오는 수]
dp = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] = 1

for j in range(2,n+1):
    for i in range(10):
        # 맨 뒷자리가 0인 경우 -> 직전이 1
        if i == 0:
            dp[j][i] = dp[j-1][1]
        # 맨 뒷자리가 9인 경우 -> 직전이 8
        elif i == 9:
            dp[j][i] = dp[j-1][8]
        # 나머지
            # 맨 뒷자리가 3인 경우 -> 직전이 2 or 4
        else:
            dp[j][i] = dp[j-1][i-1] + dp[j-1][i+1]
            
print(sum(dp[n])%(1000000000))
            
