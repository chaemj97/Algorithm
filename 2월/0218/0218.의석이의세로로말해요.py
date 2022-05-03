import sys
sys.stdin = open('sample_input.의석.txt')

# T : 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # 각 테스트 케이스는 총 다섯 줄로 이루어져 있음
    arr = [input() for _ in range(5)]

    # 세로로 읽기
    # 비어있으면 -> IndexError -> Except처리
    result = ''
    for j in range(15):
        for i in range(5):
            try:
                result += arr[i][j]
            except:
                result += ''
    print(f'#{tc} {result}')

    # 유라 1
    # 세로로 읽기
    #  i행의 길이가 j인덱스보다 길어야 빈공간이 아님
    sols = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                sols += arr[i][j]
    print(f'#{tc} {sols}')