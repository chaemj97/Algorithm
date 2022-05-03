import sys
sys.stdin = open('sample_input_5.txt')

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 소인수분해할 숫자
    N = int(input())

    # i로 나누었을 때 나머지가 0이라면 지수 1 추가 + N을 i로 나누기
    # N이 1일때까지 반복
    result = [0]*5
    while N != 1:
        if N%2 == 0:
            N = N/2
            result[0] += 1
        if N%3 == 0:
            N = N/3
            result[1] += 1
        if N%5 == 0:
            N = N/5
            result[2] += 1
        if N%7 == 0:
            N = N/7
            result[3] += 1
        if N%11 == 0:
            N = N/11
            result[4] += 1

    print(f'#{tc }', *result)

    # 유라
    # 밑
    lst = [2,3,5,7,11]
    cnt =[0]*5
    # i(밑)으로 나누었을 때 나머지가 0이면 지수 1 추가 + N으로 나누기
    # i로 나누어지지 않을 때까지
    for i in range(5):
        while N % lst[i] == 0:
            cnt[i] += 1
            N //= lst[i]
    print(f'#{tc}', *cnt)