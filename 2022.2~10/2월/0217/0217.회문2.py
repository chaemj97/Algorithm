import sys
sys.stdin = open('input.회문2.txt')

# M : 회문 길이, arr : 리스트
# 회문 있으면 True, 없으면 False
def palindrome(M, arr):
    for i in range(100):
        # 가로 회문
        for j in range(0, 100-M+1):
            # 구간 M에서 양 끝 값이 같을 때만 안쪽 확인
            if arr[i][j] == arr[i][j+M-1]:
                # 안쪽 확인
                # 다르면 멈추기
                # 모두가 같으면 True 반환
                for k in range(1, M//2):
                    if arr[i][j+k] != arr[i][j+M-1-k]:
                        break
                else:
                    return True

        # 세로 회문
        for j in range(0, 100-M+1):
            if arr[j][i] == arr[j+M-1][i]:
                for k in range(1, M//2):
                    if arr[j+k][i] != arr[j+M-1-k][i]:
                        break
                else:
                    return True
    return False

T = 10
for tc in range(1,T+1):
    # N : 테스트 케이스의 번호, arr : 테스트 케이스
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    # M : 회문의 길이
    for M in range(100, -1, -1):
        # 회문 있으면 True, 그 때 M이 회문의 최대 길이
        if palindrome(M, arr):
            print(f'#{tc} {M}')
            break

