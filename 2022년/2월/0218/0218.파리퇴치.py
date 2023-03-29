import sys
sys.stdin = open('input.파리.txt')

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 배열, M*M 파리채 크기
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 최대값
    max_v = 0
    # (0,0) -> (N-M,N-M) 까지 확인하기
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            # 사각형 크기 M*M
            for x in range(i,i+M):
                for y in range(j,j+M):
                    cnt += arr[x][y]
            # 합의 최댓값 찾기
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')