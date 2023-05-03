'''
    접근법 1
        전깃줄이 안꼬일려면 전깃줄 끝이 오름차순이면 된다.
        LIS 알고리즘 이용
'''

import sys
input = sys.stdin.readline

# 전깃줄의 개수
n = int(input())
line = [list(map(int,input().split())) for _ in range(n)]

# 전깃줄 시작 위치 오름차순으로 정렬
line.sort(key=lambda x: x[0])

a = []
for l in line:
    a.append(l[1])

# dp
dp = [0]*(n+1)
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i],dp[j])
    dp[i] += 1

print(n - max(dp))