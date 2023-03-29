

# 아무것도 붙이지 않는 경우 1
def solve(N):
    if N < 2:
        return 1
    return solve(N-1) + solve(N-2)*2

# bottom
def solve2(N):
    # 10 <= N <= 300
    result = [0]*30
    result[0] = 1
    result[1] = 1
    for i in range(2,N+1):
        result[i] = result[i-1] + result[i-2]*2
    return result[N]

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 테스트 케이스
    N = int(input())//10
    result = solve(N)
    print(f'#{tc} {result}')




