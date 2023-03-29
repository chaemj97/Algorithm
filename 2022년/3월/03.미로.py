# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 미로
    N = int(input())
    maze = [list(map(int,input().rstrip('\r'))) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r,c = i,j
                break
    # 이동경로
    stack = []
    # 방문확인
    visited = [[0]*N for _ in range(N)]
    # 시작점 표시
    stack.append((r,c))
    visited[r][c] = 1

    # 이동방향 오, 아, 왼, 위
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    # 결과 : 도착하면 1, 아니면 0 (기본값 = 도착 못 함)
    result = 0

    # 스택이 비었다는 건 갈 수 있는 길이 없어 되돌아오면서 길을 탐색해도 길이 없음
    while stack:
        # 현재 위치
        cr,cc = r,c
        # 위치 값이 3이면 도착
        if maze[cr][cc] == 3:
            result = 1
            break

        # 길을 따라 이동해보기
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 갈 수 있는 길인지 확인
            # 갈 수 없는 길 : 미로를 벗어나는 경우, 벽, 이미 방문한 곳
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                # 갈 수 있는 길이니 이동해보기
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        # break을 만나지 않았다는 것은 갈 길이 없다는 것 -> 한 칸 되돌아 가보자
        else:
            stack.pop()

    print(f'#{tc} {result}')