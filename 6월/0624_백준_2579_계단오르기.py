n = int(input())
stair = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(stair[-1])
else:
    dp = [0] * (n + 1)
    dp[0] = stair[0]
    dp[1] = max(stair[0] + stair[1], stair[1])
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])
    print(dp[-1])

# from sys import stdin
# input = stdin.readline

# # 계단의 개수
# N = int(input())
# step = [int(input()) for _ in range(N)]

# max_score = 0
# # 현재 계단 위치, 얻은 점수, 밟은 연속된 계단 수
# def upstep(idx,score,cnt):
#     global max_score
#     # 마지막 도착 계단 밟기
#     if idx == N-1:
#         # 얻은 총 점이 최대값인가?
#         if score > max_score:
#             max_score = score
#         return
#     if cnt < 2:
#         upstep(idx+1, score + step[idx], cnt+1)
#     if idx +2 < N:
#         upstep(idx+2, score + step[idx], 1)
   
# upstep(-1,0,0)

# print(max_score)        