'''
    접근법
        dp : 2*n 배열
        
        dp[0][j] : 점프를 하지 않고 j에 도달했을 때 밟은 블록 수
        dp[1][j] : 점프 1번 하고 j에 도달했을 때 밟은 블록 수
        
        1. 이동 가능
            1. 이동
                dp[0][i] = dp[0][i-1] + 1
                dp[1][i] = dp[1][i-1] + 1
            
        2. 이동 불가능
            1. 처음부터 시작
                dp[0][i] = 1
            2. 점프 1회 쓰기
                dp[1][i] = dp[0][i-1] + 1
'''

import sys
input = sys.stdin.readline

# 블럭 수, 보폭 크기
n,k = map(int,input().split())
# 보도블럭 사이 거리
l = [0]+list(map(int,input().split()))

# dp[0][j] : 점프를 하지 않고 j에 도달했을 때 밟은 블록 수
# dp[1][j] : 점프 1번 하고 j에 도달했을 때 밟은 블록 수
dp = [[0]*n for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1

for i in range(1,n):
    # 이동 가능
    if l[i] <= k:
        dp[0][i] = dp[0][i-1] + 1
        dp[1][i] = dp[1][i-1] + 1
    # 이동 X -> 점프
    else:
        # 점프 X -> 처음부터 시작
        dp[0][i] = 1
        # 점프하기
        dp[1][i] = dp[0][i-1] + 1

# 정답
answer = max(max(dp[0]),max(dp[1]))
print(answer)