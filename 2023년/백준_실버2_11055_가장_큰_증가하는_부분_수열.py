'''
    접근법 1
        LIS 알고리즘 활용
'''

import sys
input = sys.stdin.readline

A = int(input())
arr = list(map(int,input().split()))

dp = arr[:]
for i in range(A):
    for j in range(i):
        if arr[i]  > arr[j]:
            dp[i] = max(dp[i],dp[j]+arr[i])
            
print(max(dp))