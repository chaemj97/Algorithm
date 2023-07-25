'''
    접근법
        1. 팰린드롬 구하기
            길이가 1
            길이가 2
            길이가 3이상
        2. 분할 횟수 구하기
            
    
'''
import sys
input = sys.stdin.readline

s = list(input().rstrip())
n = len(s)
# pal[i][j] : s[i]에서 s[j]까지 팰린드롬
pal = [[0]*(n) for _ in range(n)]

# 팰린드롬 구간 구하기

# 팰린드롬 길이가 1
for i in range(n):
    pal[i][i] = 1
# 팰린드롬 길이가 2
for i in range(1,n):
    if s[i-1] == s[i]:
        pal[i-1][i] = 1
# 팰린드롬 길이가 3이상
for size in range(2,n+1):
    # 시작점
    for i in range(n-size):
        if s[i] == s[i+size] and pal[i+1][i+size-1] == 1:
            pal[i][i+size] = 1

# 분할 숫자 세기
dp = [0]*n
dp[0] = 1

for i in range(1,n):
    min_value = dp[i-1]+1
    for j in range(i):
        if pal[j][i]:
            min_value = min(min_value,dp[j-1]+1)
    dp[i] = min_value
# 결과 출력
print(dp[-1])