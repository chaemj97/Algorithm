# (r,c) : 현재 위치, s : 지나온 길 숫자 합
def check(r,c,s):
    global min_sum
    # 도착?
    if r == N-1 and c == N-1:
        if min_sum > s:
            min_sum = s
        return

    # 최솟값을 구하는 것이니 이미 이전 최솟값보다 크면 계산 필요X
    if s > min_sum:
        return

    # 이동
    for dr,dc in [[0,1],[1,0]]:
        # 범위 내
        if 0<=r+dr<N and 0<=c+dc<N:
            check(r+dr,c+dc,s+arr[r+dr][c+dc])

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 숫자 판
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 1000000000
    check(0,0,arr[0][0])

    print(f'#{tc} {min_sum}')