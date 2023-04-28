'''
    접근법 1
        목표 : n을 최소 개수의 제곱수 합으로 표현

'''
import sys
input = sys.stdin.readline

''' 
# 모든 경우 다 구하기 ->실패

from itertools import combinations
n = int(input())
num = [i**2 for i in range(int(n**0.5),0,-1)]
for i in range(1,5):
    for c in combinations(num,i):
        if sum(c) == n:
            print(i)
            sys.exit(0)
'''

n = int(input())
dp = [5]*(n+1)
dp[0] = 0

# n 최대 50000
# n**0.5 최대 223
# n * n**0.5 최대 11,150,000

for i in range(n+1):
    for j in range(1,(int(i**0.5)+1)):
        # i에 j**2이 들어가는게 더 적은 개수의 제곱합인가?
        dp[i] = min(dp[i],dp[i-j**2]+1)
    
print(dp[n])