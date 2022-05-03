# 유라 풀이 다시보기
def BFS(i,j):
    tn,tc = 0,arr[i][j]
    q = []
    q.append((i,j))
    # 이동가능 방향
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    while q:
        # 현재 위치
        ci, cj = q.pop()
        for i in range(4):
            di = ci + dr[i]
            dj = cj + dc[i]
            # 범위 내, 방문 X, 1차이
            if 0 <= di < N and 0 <= dj < N and not visited[di][dj] and arr[di][dj] - arr[ci][cj] == 1:
                q.append((di,dj))
                visited[di][dj] = 1
        else:
            break


    return

# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    # 방문했는가
    visited = [[0]*N for _ in range(N)]

    # 이동할 수 있는 방의 최댓값
    cnt = 0
    # 이동할 수 있는 방의 개수가 최대인 방이 여럿이면 그 중 작은거
    num = N*N

    for i in range(N):
        for j in range(N):
            # 방문한 적 없으면
            if not visited[i][j]:
                tc,tn  = BFS(i,j)
                if cnt <= tc and num>tn:
                    cnt = tc
                    num = tn
    print(f'#{tc} {num} {cnt}')