# https://chaemi720.tistory.com/197

from sys import stdin
input = stdin.readline

# 근무 일
N = int(input())
# 상담 [걸리는 시간, 받을 수 있는 금액]
counsel = [list(map(int,input().split())) for _ in range(N)]

# 각 근무일까지 얻을 수 있는 최대 이익
dp = [0 for _ in range(N+1)]

for day in range(N-1,-1,-1):
    # 해당 일의 상담을 근무 종료 전 마무리 가능한 경우
    if day + counsel[day][0] <= N:
        # 근무를 하는 경우 / 근무를 하지 않는 경우 중 최대 이익이 나는 것 고르기
        dp[day] = max(dp[day+1],dp[day+counsel[day][0]] + counsel[day][1])
    # 해당 일의 상담을 근무 종료 전 마무리 불가능 한 경우
    else:
        dp[day] = dp[day+1]

print(dp[0])