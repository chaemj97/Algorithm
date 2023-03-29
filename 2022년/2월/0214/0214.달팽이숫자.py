# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N크기의 달팽이
    N = int(input())
    # N*N 크기 판
    result = [[0]*N for _ in range(N)]

    # 이동방향 우,하,좌,상
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    # 다음 칸으로 이동하기 위한 방향을 나타내는 변수
    # 0: 우, 1: 하, 2: 좌, 3: 상
    dir =0 # 최초는 오른쪽으로 이동
    r, c = 0, 0 # 현재 위치
    num = 1

    # N*N 행렬에 1부터 N*N 까지 정수를 하나씩 넣기
    # 숫자를 행렬에 다 넣을 때 까지 계속 반복
    # 이동하고, 숫자 넣기
    while num <= N*N:

        # 정상 범위이고 다른 숫자가 없으면, 숫자할당
        if (0 <= r < N and 0 <= c < N) and result[r][c] == 0:
            result[r][c] = num
            num += 1

        # 정상 범위가 아니면 이동방향 바꾸기, 정상범위 안으로 돌리기
        else:
            # 이전으로 이동
            r -= dr[dir]
            c -= dc[dir]
            # 방향 바꾸기
            dir = (dir + 1) % 4

        # 다음으로 이동
        r += dr[dir]
        c += dc[dir]

    print(f'#{tc}')
    for row in result:
        print(*row)