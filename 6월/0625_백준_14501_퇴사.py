# N = int(input())
# li = [list(map(int, input().split())) for _ in range(N)]
# dp = [0 for _ in range (N+1)]

# for i in range(N-1, -1, -1):
#     if i + li[i][0] > N:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])
    
# print(dp[0])

from sys import stdin
input = stdin.readline

# 상담일
N = int(input())
counsel = [list(map(int,input().split())) for _ in range(N)]

# 얻을 수 있는 최대 이익
max_profit = 0

def check(idx,profit):
    global max_profit
    # 상담 일정을 다 세웠는가?
    if idx == N:
        # 최대 수익인가?
        if profit > max_profit:
            max_profit = profit
        return
    # 상담 일정 세우기
    for t,p in counsel[idx:]:
        # 퇴사 전에 마무리 가능한 상담인가
        if idx + t < N:
            check(idx+t,profit+p)
    else:
        return

check(0,0)
print(max_profit)
