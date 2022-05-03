import sys
sys.stdin = open("input.sum.txt")

for tc in range(1,11):
    # 테스트 케이스 번호
    N = int(input())
    # 2차원 배열
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    # 행 합, 열 합 중 가장 큰 값 찾기
    for i in range(100):
        # 가로 합
        sum_row = 0
        # 세로 합
        sum_column = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_column += arr[j][i]

        if result < sum_row:
            result = sum_row
        if result < sum_column:
            result = sum_column

    # 대각선 합 구하기
    # 오른쪽 아래로 가는 대각선 합
    a = 0
    # 오른쪽 위로 가는 대각선 합
    b = 0
    for k in range(100):
        a += arr[k][k]
        b += arr[k][100 - 1 - k]

    # 행 합, 열 합, 대각선 합 중 큰 값 찾기
    if result < a:
        result = a
    if result < b:
        result = b

    print(f'#{tc} {result}')