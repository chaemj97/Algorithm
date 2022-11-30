# https://chaemi720.tistory.com/183

from sys import stdin
input = stdin.readline

# 계단의 수
N = int(input())
# 각 계단에 쓰여 있는 점수 (stair[0] : 바닥, stair[1] : 1번 계단)
stair = [0] + [int(input()) for _ in range(N)]

# 1칸짜리 계단이면 1가지 경우의 수
if N == 1:
    print(stair[1])
else:
    # dp[i] = i번째 계단까지 올랐을 때 얻을 수 있는 점수 최댓값
    dp = [0]*(N+1)
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]
    # 2칸으로 올라온 것/ 1칸으로 올라온 것 중 최대값
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3,N+1):
        # 1칸 올라올려면 그 전에 2칸으로 올라와야함
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

    print(dp[N])

