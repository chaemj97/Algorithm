# T : 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    # 칠할 영역의 개수
    N = int(input())

    # 10*10 격자
    arr = [[0] * 10 for _ in range(10)]
    # 보라색 영역 개수
    result = 0

    for i in range(N):
        # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color
        r1, c1, r2, c2, color = map(int, input().split())
        # 격자에 빨간색이면 1 추가, 파란색이면 2 추가 -> 값이 3인 격자 = 보라색
        # 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    result += 1
    print(f'#{tc} {result}')