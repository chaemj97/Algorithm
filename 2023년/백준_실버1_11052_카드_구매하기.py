'''
    접근법
        dp를 사용하여 'k개 카드팩'을 사는 경우/사지 않는 경우 중 최대 고르기    
'''
import sys
input = sys.stdin.readline

# 구매 카드 개수
n = int(input())
# p[k] : k개 카드가 들어 있는 카드팩 가격
p = [0] + list(map(int,input().split()))

# dp[i] : 카드 i개 구매하는 최대 가격
dp = [0]*(n+1)

for i in range(1,n+1):
    for k in range(1,i+1):
        # k개 들어있는 카드팩을 사지 않는 경우 / 사는 경우 중 최대
        dp[i] = max(dp[i],p[k]+dp[i-k])
        
print(dp[n])