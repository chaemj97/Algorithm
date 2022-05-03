import sys
sys.stdin = open('input.어디.txt')

def count_arr(N):
    sol = 0
    for i in range(N + 1):
        cnt = 0
        for j in range(N + 1):
            # 1이면 cnt 추가
            if arr[i][j] == 1:
                cnt += 1
            # 0이면 길이 확인하기
            else:
                # 길이가 K이면 단어 들어갈 수 있음
                if cnt == K:
                    sol += 1
                cnt = 0
    return sol

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 크기의 단어 퍼즐, K : 단어의 길이
    N, K = map(int,input().split())
    # 0 추가
    arr = [list(map(int,input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1))
    # 행방향 체크
    sol = count_arr(N)
    # 열방향 체크
    # 전치행렬
    arr = list(map(list,zip(*arr)))
    sol += count_arr(N)
    print(f'#{tc} {sol}')