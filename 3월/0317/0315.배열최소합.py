def min_v(idx, sum_v):
    global min_sum
    # 최솟값보다 크면 필요없음
    if sum_v >= min_sum:
        return
    # 모든 열에서 1개씩 고름
    if idx == N:
        if min_sum > sum_v:
            min_sum = sum_v
            return
    # 각 열에서 고르기
    for i in range(N):
        if not col_used[i]:
            col_used[i] = 1
            min_v(idx + 1, sum_v + arr[idx][i])
            # 복구
            col_used[i] = 0

# 테스트 케이스 개수
T = int(input())
for tc in range(1, 1 + T):
    # N*N 배열
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 열을 사용했는가
    col_used = [0] * N
    min_sum = 100000
    min_v(0, 0)
    print(f'#{tc} {min_sum}')