import sys
sys.stdin = open('im예제.txt')
# 테스트 케이스 개수

T = int(input())
for tc in range(1,T+1):
    # 배열의 크기
    N = int(input())
    ARR = [list(input()) for _ in range(N+1)]

    # H : 집,X : 아무것도 없음
    # 동서남북 커버 기지국 A : 1개씩, B : 2개씩, C : 3개씩

    # 마지막줄을 필요 없음
    for r in range(N):
        for c in range(N):
            # if ARR[r][c] == 'X' or ARR[r][c] == 'H':
            #     continue
            k =0
            if ARR[r][c] == 'A':
                k = 1
            elif ARR[r][c] == 'B':
                k = 2
            elif ARR[r][c] == 'C':
                k = 3

            for i in range(1,k+1):
                # 상
                if r-i >= 0 and ARR[r-i][c] == 'H':
                    ARR[r - i][c] = 'o'
                # 하
                if r + i <= N-1 and ARR[r + i][c] == 'H':
                    ARR[r + i][c] = 'o'
                # 좌
                if c - i >= 0 and ARR[r][c-i] == 'H':
                    ARR[r][c-i] = 'o'
                # 우
                if c + i <= N-1 and ARR[r][c+i] == 'H':
                    ARR[r][c+i] = 'o'

    cnt = 0
    for r in range(N):
        for c in range(N):
            if ARR[r][c] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')

    # 답 442
