# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 신청수
    N = int(input())
    # 작업 시작 시간, 종료 시간
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 종료 시간 기준으로 내림차순 정렬
    arr.sort(key=lambda x: x[1])
    # 이전 종료 시간
    end = 0
    cnt = 0
    for s,e in arr:
        # 시작 시간이 이전 종료 시간보다 늦어야함(같아도 됨)
        if s >= end:
            end = e
            cnt += 1
    print(f'#{tc} {cnt}')