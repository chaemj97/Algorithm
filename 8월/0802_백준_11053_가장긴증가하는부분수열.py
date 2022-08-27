from sys import stdin
input = stdin.readline

# 부분수열이란 원래 수열에서 일부 항들을 택하면서 "순서를 유지하여" 만든 수열
N = int(input())
arr = list(map(int,input().split()))

dp = [0]*N
for i in range(N):
    # i에서 도착
    dp[i] = 1
    for j in range(0,i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))
