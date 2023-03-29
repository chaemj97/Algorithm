# current : 현재 위치, cnt : 충전 횟수
def check(current,cnt):
    global min_cnt
    # 이미 충전 횟수가 많다? -> 버려
    if cnt >= min_cnt:
        return
    # 도착?
    if current >= N:
        # 최소 충전인가?
        if cnt <= min_cnt:
            min_cnt = cnt
        return
    # 이동
    for i in range(M[current],0,-1):
        check(current+i,cnt+1)

# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi
    M = list(map(int,input().split()))
    N = M[0]

    min_cnt = 100000000000
    # 1에서 충전은 충전 횟수로 치지 않으므로 충전 횟수 시작은 -1
    check(1,-1)

    print(f'#{tc} {min_cnt}')