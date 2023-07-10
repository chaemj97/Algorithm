'''
    접근법
        dp를 사용하여 자신보다 작은 수 세기
    
'''
import sys
input = sys.stdin.readline

# 수열의 크기
n = int(input())
A = list(map(int,input().split()))

dp = [1 for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        # 뒤의 수가 더 작다면
        if A[i] > A[j]:
            dp[j] = max(dp[i]+1,dp[j])
            
print(max(dp))