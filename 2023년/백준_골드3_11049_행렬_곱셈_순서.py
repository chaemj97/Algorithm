'''
    접근법
        행렬 4개인 경우
        AB
        BC -> ABC : min(AB*C, A*BC) 
        CD -> BCD : min(BC*D, B*CD) -> ABCD : min(ABC*D, A*BCD)

        2개씩 곱한다고 생각하기
'''

import sys
input = sys.stdin.readline

# 행렬의 수
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
# cnt : 곱한 행렬의 수
for cnt in range(2,n+1):
    # 행렬곱 시작 행렬 위치
    # cnt == 2 -> i : 0 ~ n-2
        # dp[0][1], dp[1][2], ... , dp[n-2][n-1]
    # cnt == 3 -> i : 0 ~ n-3
        # dp[0][2], dp[1][3], ... , dp[n-3][n-1]
    for i in range(n-cnt+1):
        # i번째 행렬부터 연속된 cnt개 행렬 곱
        dp[i][i+cnt-1] = 2**31 # 최댓값
        # k+1번째 끊겨있으므로 연결하기
        for k in range(i,i+cnt-1):
            dp[i][i+cnt-1] = min(dp[i][i+cnt-1],
                                 # 두 행렬 곱 연결
                                 dp[i][k]+dp[k+1][i+cnt-1]+matrix[i][0]*matrix[k][1]*matrix[i+cnt-1][1])

print(dp[0][n-1])