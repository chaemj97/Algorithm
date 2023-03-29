# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산

# idx : 공장 번호, used : 제품 생산 여부, cost : 생산 비용
def check(idx,used,cost):
    global min_cost
    # 이미 최소 생산 비용보다 큰가?
    if cost >= min_cost:
        return
    # N개 선택?
    if idx == N:
        # 최소 생산 비용인가?
        if min_cost > cost:
            min_cost = cost
        return
    for i in range(N):
        # 생산한 적?
        if used[i] == 0:
            # 생산 체크
            used[i] = 1
            check(idx+1,used,cost+V[idx][i])
            # 되돌리기
            used[i] = 0


# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 제품 수
    N = int(input())
    # 공장별 생산비용
    V = [list(map(int,input().split())) for _ in range(N)]

    # 최소 생산 비용
    min_cost = 100000000
    check(0,[0]*N,0)

    print(f'#{tc} {min_cost}')