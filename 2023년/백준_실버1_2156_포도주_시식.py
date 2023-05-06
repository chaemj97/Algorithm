'''
    접근법
        dp[n]은
            1. n번째 포도주를 마신 경우
                1) n-1번째 포도주를 마신 경우 -> n-2번째 포도주 X -> n-3번째 포도주를 마실 수 있다.
                    : dp[n-3] + arr[n-1] + arr[n]
                2) n-1번째 포도주를 마시지 않은 경우 -> n-2번째 포도주를 마실 수 있다. 
                    : dp[n-2] + arr[n]
            2. n번째 포도주를 마시지 않은 경우 
                : dp[n-1]
        3가지 경우 중 최댓값 선택하기
    
'''
import sys
input = sys.stdin.readline

# 포도주의 잔의 개수
n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0]*n
dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0]+arr[1]
if n > 2:
    # 0,1 선택 / 0,2 선택 / 1,2 선택
    dp[2] = max(dp[1],arr[0]+arr[2],arr[1]+arr[2])
for i in range(3,n):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i],
                dp[i-2] + arr[i],
                dp[i-1])
print(dp[n-1])
