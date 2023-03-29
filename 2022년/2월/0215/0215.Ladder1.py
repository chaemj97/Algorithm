import sys
sys.stdin = open("input.Ladder1.txt")

T = 10
for tc in range(1,T+1):
    # N : 테스트 케이스의 번호
    N = int(input())
    # arr : 1-사다리, 0-여백, 2-도착지점
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 도착지점에서 거꾸로 찾아가기

    # 도착지점 2가 어디에 있는지 idx 찾기
    # end : 사다리 결과 도착지점, 거꾸러 찾아가는 길의 시작지점
    end_r = 99
    end_c = 0
    for j in range(100):
        if arr[99][j] == 2:
            end_c = j

    # 오른쪽 or 왼쪽에 1 있을 경우 따라서 이동
    # 없으면 위로 이동

    # 위에 아무것도 없다면(arr[0][]) 이면 멈춰서 그 자리의 열의 위치 말하기
    while end_r != 0:
        # 오른쪽이 1이면 오른쪽에 0이 나올때까지 이동 + 위로 한 칸 이동
        if 0 <= end_c+1 <=99 and arr[end_r][end_c+1]:
            while end_c+1 <= 99 and arr[end_r][end_c+1]:
                end_c += 1
            end_r -= 1
        # 왼쪽이 1이면 왼쪽에 0이 나올때까지 이동 + 위로 한 칸 이동
        elif 0 <= end_c-1 <=99 and arr[end_r][end_c-1]:
            while 0 <= end_c-1 and arr[end_r][end_c-1]:
                end_c -= 1
            end_r -= 1
        # 옆에 1이면 위로 이동
        else:
            end_r -= 1

    print(f'#{N} {end_c}')
