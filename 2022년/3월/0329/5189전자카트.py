# idx : 방문 횟수, k : 현재 위치
def check(idx,s,k):
    global min_sum
    # 도착?
    if idx == N:
        # 되돌아오기
        s += arr[k][0]
        if min_sum > s:
            min_sum = s
        return
    # 최솟값을 구하는 것이니 이미 이전 최솟값보다 크면 계산 필요X
    if s > min_sum:
        return
    for i in range(1,N):
        if used[i] == 0: # 방문한 적 X
            used[i] = 1 # 방문표시
            check(idx+1,s+arr[k][i],i)
            used[i] = 0

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # r->c 이동시 베터리 소모량 arr[r][c]
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 10000000000
    # 방문 표시
    used = [0]*N
    used[0] = 1
    check(1,0,0)

    print(f'#{tc} {min_sum}')