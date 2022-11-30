for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = -2100000000

    # 1. 행 우선순회 하면서 각 행의 합 구하기
    for i in range(100):
        # 행 순회 시작점에서 합을 구하기 위한 변수 초기화
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        # 반복문이 끝난시점 : row_sum -> 한 행의 합이 저장되어 있음
        # 최대 합만 저장
        max_sum = row_sum if row_sum > max_sum else max_sum

    # 2. 열 우선순회 합구하기
    for i in range(100):
        # 열 순회 시작점에서 합을 구하기 위한 변수 초기화
        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]
        # 반복문이 끝난시점 : row_sum -> 열 행의 합이 저장되어 있음
        # 최대 합만 저장
        max_sum = col_sum if col_sum > max_sum else max_sum

    # 3.대각선 순회
    # r == c , 대각선 1
    # r + c == 99 대각선 2
    dia1_sum = 0
    dia2_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                dia1_sum += arr[i][j]
            if i + j == 99:
                dia2_sum += arr[i][j]
    max_sum = dia1_sum if dia1_sum > max_sum else max_sum
    max_sum = dia2_sum if dia2_sum > max_sum else max_sum

    print(f'#{tc} {max_sum}')
