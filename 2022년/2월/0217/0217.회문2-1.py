import sys
sys.stdin = open('input.회문2.txt')

# arr : 리스트
def palindrome(arr):
    # M: 회문길이
    for M in range(100,1,-1):
        for i in range(100):
            # 가로 회문
            for j in range(0, 100 - M + 1):
                # 구간 M에서 양 끝 값이 같을 때만 안쪽 확인
                if arr[i][j] == arr[i][j + M - 1]:
                    # 안쪽 확인
                    # 다르면 멈추기
                    # 모두가 같으면 M 반환
                    for k in range(1, M // 2):
                        if arr[i][j + k] == arr[i][j + M - 1 - k]:
                            break
                    else:
                        return M

            # 세로 회문
            for j in range(0, 100 - M + 1):
                if arr[j][i] == arr[j + M - 1][i]:
                    for k in range(1, M // 2):
                        if arr[j + k][i] != arr[j + M - 1 - k][i]:
                            break
                    else:
                        return M
    return False


T = 10
for tc in range(1, T + 1):
    # N : 테스트 케이스의 번호, arr : 테스트 케이스
    N = int(input())
    arr = [list(input()) for _ in range(100)]

    result = palindrome(arr)
    print(f'#{tc} {result}')