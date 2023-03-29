import sys
sys.stdin = open('input.미로1.txt')

for _ in range(10):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    # 0: 통로, 1 : 벽, 2 : 출발지점, 3: 도착지점

    # 출발지점 찾기
    for i in range(1,16):
        for j in range(1,16):
            if maze[i][j] == 2:
                r,c =i,j
                break
    # 지나간 길 표시
    stack = []
    stack.append((r,c))
    # 방문 표시
    visited = [[0]*16 for _ in range(16)]
    visited[r][c] = 1
    # 이동가능방향 4방향
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 기본값은 미로 도달 불가
    result = 0
    while stack:
        # 현재위치
        cr,cc = stack[-1]
        # 도착?
        if maze[cr][cc] == 3:
            result = 1
            break

        # 4방향 확인
        for d in range(4):
            ddr = cr + dr[d]
            ddc = cc + dc[d]
            # 범위내에 있고, 0이고 방문한적 없어야 이동가능,
            if 0 <= ddr < 16 and 0 <= ddc <16 and maze[ddr][ddc] != 1 and not visited[ddr][ddc]:
                stack.append((ddr,ddc))
                visited[ddr][ddc] = 1
                break
        # 4방향 모두 갈 수 없으면 1칸 되돌아가보자
        else:
            stack.pop()

    print(f'#{tc} {result}')