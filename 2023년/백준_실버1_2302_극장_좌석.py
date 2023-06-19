'''
    접근법
        seat[1] = 1
        seat[2] = 2
        1 2
        2 1
        seat[3] = 3
        1 2 3
        2 1 3
        1 3 2
        seat[4] = 5
        1 2 3 4 
        2 1 3 4
        1 3 2 4
        1 2 4 3
        2 1 4 3
        seat[i] = seat[i-1] + seat[i-2]
        i번 자리 i번이 앉기 + 앉지 않기
'''
import sys
input = sys.stdin.readline

# 좌석의 수
n = int(input())
# 고정석 개수
m = int(input())
# 고정석
vip = list(int(input()) for _ in range(m))

# vip 없이 앉는 경우의 수
dp = [0]*(n+1)
dp[0],dp[1] = 1,1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
# vip 생각하기
answer = 1
# vip 존재
if m > 0:
    # 각 vip 사이 경우의 수 곱하기
    
    # 직전 vip 위치
    pre_vip = 0
    for j in range(m):
        # vip 사이 자리 개수
        s = vip[j] - pre_vip - 1
        # s명 자리 변경 가능 경우의 수
        answer *= dp[s]
        pre_vip = vip[j]
    answer *= dp[n - pre_vip]    
# vip 없음
else:
    answer = dp[n]
print(answer)