import sys
sys.stdin = open("input.Ladder1.txt")

T = 10
for _ in range(1,T+1):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # 사다리 타기 시작
    # 0행을 검사를 해서 시작점이라면(1이라면) 시작

    # 아래쪽, 오른쪽, 왼쪽
    dr = [1, 0, 0]
    dc = [0, 1, -1]

    result = 0

    for i in range(100):
        if ladder[0][i]: # 시작점 찾음
            # 현재 위치를 r, c로 저장
            # 움직이는 방향을 지정 : 0아래쪽, 1오른쪽, 2왼쪽
            # 현재 위치 + 움직이는 방향에 대한 변화량 더하기
            # 방향을 바꾸어야 하는 경우가 생기면 방향 바꾸기
                # 움직이는 방향 : 아래쪽 > 좌 or 우 갈 수 있음
                #               좌 or 우 > 아래쪽으로 갈 수 있음
            # 만약에, r이 99라면 멈춰!!
            # 현재위치
            r, c = 0, i
            d = 0
            while r < 99:
                # 움직이기 전에 방향을 바꾸는 경우가 있는지 검사
                # 움직이고 있는 방향에 따라서 방향을 바꾸는 검사가 다름

                if d == 0: # 아래쪽 방향으로 움직이고 있었다면
                    # 좌, 우 검사 << 양쪽에 0이 있으면 내려가기
                    if c > 0 and ladder[r][c-1]: # 왼쪽으로 갈 수 있을 때
                        d = 2
                    elif c < 99 and ladder[r][c+1]: # 오른쪽으로 갈 수 있을 때
                        d = 1

                else: # 좌 or 우 방향으로 움직이고 있을 떄
                    if ladder[r+1][c]: # 아래쪽으로 갈 수 있을 때
                        d = 0

                # 현재 움직이는 방향에 대해서 변화량 더하기
                r += dr[d]
                c += dc[d]

            # r이 99가 되면서 반복이 끝난 시점에서 ladder[r][c] == 2 라면,
            # i가 정답
            if ladder[r][c] == 2:
                result = i
                break # 정답을 찾았으니 끝

    print(f'#{tc} {result}')