'''
    접근법
        25114
        dp[n] : n자리 수까지 가능한 경우의 수
        dp[0] = 1 : 
        dp[1] = 1 : (2)
        dp[2] = 2 : (2,5) (25)
        dp[3] = 2 : (2,5,1) (25,1)
        dp[4] = 4 : (2,5,1,1) (2,5,11) (25,1,1) (25,11 )
        dp[5] = 6 : (2,5,1,1,4) (2,5,1,14) (2,5,11,4) (25,1,1,4) (25,1,14) (25,11,4) 
        
        1. code[i]가 단독 사용
        2. code[i]가 code[i-1]가 결합하여 사용
            10 <= code[i-1]*10 +code[i] < 27
'''
import sys
input = sys.stdin.readline

code = [0]+list(map(int,input().rstrip()))
# 암호가 0으로 시작할 수 X
if code[1] == 0:
    print(0)
    sys.exit()

dp = [0]*(len(code))
dp[0], dp[1] = 1, 1
for i in range(2,len(code)):
    # 1. code[i]가 단독으로 존재
    if code[i] != 0:
        dp[i] += dp[i-1]
    # 2. code[i]가 앞 수와 결합하여 존재
    if 10 <= code[i-1]*10+code[i] < 27:
        dp[i] += dp[i-2]

print(dp[-1]%1000000)