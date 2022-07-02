# https://chaemi720.tistory.com/189

# 물품의 수, 버틸 수 있는 무게
n, k = map(int, input().split())

# 여행에 필요하다고 생각하는 물건들
items = [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(k+1)]

for item in items:
    # 무게, 가치
    w,v = item
    for i in range(k,w-1,-1):
        # 이 물건을 담지 않기 / 담기 중 가치가 큰 거 선택
        dp[i] = max(dp[i],dp[i-w]+v)

print(dp[k])