'''
    접근법
        숫자 1부터 최대 1000*50 == 50,000
        1부터 확인해보자
'''

import sys
input = sys.stdin.readline

# 숫자 게임에서 사용하는 정수의 수
n = int(input())
num = list(map(int, input().split()))
# 최대 사용 횟수
k = int(input())

# 최대 만들 수 있는 수
max_num = num[-1]*k

dp = [float('inf') for _ in range(max_num+1)]

for i in range(1,max_num+1):
    # 가지고 있던 수인가?
    if i in num:
        dp[i] = 1
    # 가지지 못한 수 -> 만들어 보자
    else:
        # 이전에 만든 숫자들로 만들 수 있는가?
        # i = j + (i-j)
        # j는 1부터 i-1까지
        for j in range(1,i//2+1):
            dp[i] = min(dp[i],dp[j]+dp[i-j])
    # 숫자를 k개보다 많이 사용?
    if dp[i] > k:
        # 숫자가 홀수면 짝순이가 이김
        if i%2:
            print(f'jjaksoon win at {i}')
        # 숫자가 짝수면 홀순이가 이김
        else:
            print(f'holsoon win at {i}')
        break
                