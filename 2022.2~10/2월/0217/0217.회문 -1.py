import sys
sys.stdin = open('sample_input.회문.txt')

# 덩어리로 비교하기
def a(N,M,arr):
    k = 0
    for i in range(N):
        for k in range(N-M+1):
            # 가로 회문
            h = arr[i][k:k+M]
            # 세로 회문
            v = [arr[j][i] for j in range(k,k+M)]
            # 자신과 자신을 뒤집은 것이 같다면 회문
            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N : N*N 크기의 글자판, M : 회문의 길이
    N, M = map(int,input().split())
    # arr : 글자판
    arr = [list(input()) for _ in range(N)]

    result = a(N,M,arr)
    print(f'#{tc}',''.join(result))
