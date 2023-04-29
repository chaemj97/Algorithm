'''
    접근법 1
        가장 긴 부분 수열 길이 구하기 -> dp
        dp를 통해 구한 가장 긴 부분 수열을 거꾸로 탐색해서 가장 긴 부분 수열의 결과 구하기 

'''

import sys
input = sys.stdin.readline

# n 최대 1000
n = int(input())
A = list(map(int,input().split()))

# 가장 긴 부분 수열의 길이 구하기
dp = [1]*n
for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

# 가장 긴 부분 수열
dp_answer = max(dp)
answer = []
for i in range(n-1,-1,-1):
    if dp[i] == dp_answer:
        answer.append(A[i])
        dp_answer -= 1
answer.reverse()
print(*answer)
