def start(maze):
    # 출발지 위치
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j


for _ in range(10):
    # 테스트 케이스 번호
    tc = int(input())
    # 미로
    # 벽(1), 길(0), 출발점(2), 도착점(3)
    maze = [list(map(int,input())) for _ in range(16)]

    r,c = start(maze)

    stack = []
    stack.append((r,c))
    # 방문했던 곳 표시
    visited = [[0]*16 for _ in range(16)]
    visited[r][c] = 1

    # 기본 값 : 도착 못함
    result = 0

    while stack:
        # 현 위치
        cr,cc = stack[-1]
        # 도착?
        if maze[cr][cc] == 3:
            result = 1
            break
        # 이동
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr = cr+dr
            nc = cc+dc
            # 이동가능한 곳 -> 미로 안, 통로, 방문X
            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                # 방문 표시
                visited[nr][nc] = 1
                stack.append((nr,nc))
                break
        # 현 위치에서 갈 수 있는 길이 없다면 한 칸 되돌아가기
        else:
            stack.pop()

    print(f'#{tc} {result}')