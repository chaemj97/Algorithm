# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # 0번에서 N번까지 이동, E개의 일방통행 도로
    N, E = map(int, input().split())
    # dist[r][c] : r번에서 c번까지 이동하는데 걸리는 거리
    dist = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        dist[s][e] = w

    # 최소 이동거리
    min_dist = 10 * N
    # d[idx] : idx까지 가는데 최소 거리
    d = [0] + [min_dist] * N

    # 이동
    for i in range(N + 1):
        for j in range(N + 1):
            # i에서 j로 갈 수 있고 그 길이 최소라면
            if dist[i][j] and d[j] > d[i] + dist[i][j]:
                d[j] = d[i] + dist[i][j]

    result = d[N]
    print(f'#{tc} {result}')
