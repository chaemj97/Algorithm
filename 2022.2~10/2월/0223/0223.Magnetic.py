import sys
sys.stdin = open('input.Magnetic.txt')


# 테스트 케이스 개수
T = 10
for tc in range(1,11):
    # 정사각형 테이블의 한 변의 길이
    N = int(input())
    # 테스트 케이스
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 빨간색(1) -> S극
    # 파란색(2) -> N극
    # 열을 기준으로 볼 때
    # 빨간색(1) 나오고 파란색(2) 나오면 교착
    cnt = 0
    for c in range(N):
        isRed = False
        for r in range(N):
            if arr[r][c] == 1:
                isRed = True
            if arr[r][c] == 2 and isRed:
                cnt += 1
                isRed = False
    print(f'#{tc} {cnt}')
