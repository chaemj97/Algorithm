'''
    접근법
        dp[i][j] : i번째 앱까지 중 j비용을 들여 얻을 수 있는 최대의 byte
'''

import sys
input = sys.stdin.readline

# n개의 앱, 필요한 메모리
n,m = map(int,input().split())

# 필요한 메모리가 0이면 비활성화 할 필요 없다.
if m == 0:
    print(0)
    sys.exit()
    
# 활성화 되어 있는 앱 사용중인 메모리
app = [0] + list(map(int,input().split()))
# 비활성화 했을 경우의 비용
deactivate = [0] + list(map(int,input().split()))

# dp[i][j] : i번째 앱까지 중 j비용을 들여 얻을 수 있는 최대의 byte
dp = [[0 for _ in range(sum(deactivate)+1)] for _ in range(n+1)]
answer = sum(deactivate)

for i in range(1,n+1):
    # i번째 앱의 바이트
    byte = app[i]
    # i번째 앱을 비활성화 할 때 필요한 비용
    cost = deactivate[i]
    
    for j in range(1,sum(deactivate)+1):
        # 현재 앱을 비활성화 못함 (=> 비용 부족)
        if j < cost:
            dp[i][j] = dp[i-1][j]
        # 현재 앱 비활성화 가능
        else:
            # 비활성화 하는게 좋은지 안하는게 좋은지 비교
            dp[i][j] = max(byte+dp[i-1][j-cost],dp[i-1][j])
        
        # 조건 충족 (=> m 메모리만큼 확보)
        if dp[i][j] >= m:
            answer = min(answer,j)
            break

print(answer)