'''
    접근법
        모든 경우 다 탐색
        각 문자 매칭
            같은 경우
            다른 경우
'''
import sys
input = sys.stdin.readline

# 최장 공통 부분 수열 (부분 수열 : 순서대로)
a = list(input().rstrip())
b = list(input().rstrip())

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        # 문자가 같은 경우
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 문자가 다른 경우
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])
            