import sys
sys.stdin = open('sample_input.회문.txt')


def a(N, M, arr):
    # 가로 또는 세로의 길이가 M인 회문 찾기
    # 가로 회문 찾기
    i = 0
    j = 0
    k = 0
    result = []
    while i < N:
        if M - 1 - j + k < N:
            # 같으면 안쪽도 확인
            if arr[i][j + k] == arr[i][M - 1 - j + k]:
                j += 1
            # 다르면 첫번째 문자를 다시 지정
            else:
                j = 0
                k += 1
        # 다음 행 확인
        else:
            i += 1
            k = 0

        # 회문일 때
        if j == M // 2:
            result = arr[i][k:k + M]
            return result

    # 가로 회문 없으면 세로 회문 찾기
    i = 0
    j = 0
    k = 0
    while i < N:
        if M - 1 - j + k < N:
            # 같으면 안쪽도 확인
            if arr[j + k][i] == arr[M - 1 - j + k][i]:
                j += 1
            # 다르면 첫번째 문자를 다시 지정
            else:
                j = 0
                k += 1
        # 다음 행 확인
        else:
            i += 1
            k = 0

        # 회문일 때
        if j == M // 2:
            for s in range(k,k+M):
                result += arr[s][i]
            return result

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N : N*N 크기의 글자판, M : 회문의 길이
    N, M = map(int,input().split())
    # arr : 글자판
    arr = [list(input()) for _ in range(N)]

    result = a(N,M,arr)

    print(f'#{tc}',''.join(result))
