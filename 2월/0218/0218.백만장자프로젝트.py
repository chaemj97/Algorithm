import sys
sys.stdin = open('input.백만.txt')

# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # 연속 N일 매매가 예측 가능
    N = int(input())
    # N일간 매매가
    arr = list(map(int,input().split()))

    # # 유라 1
    # sol : 이익의 합, s = 시작인덱스, maxI : 구간에서 가장 큰 값을 가지는 것의 인덱스
    profit = s = maxI = 0
    while s < N:
        maxI = s
        for i in range(s,N):
            if arr[maxI] < arr[i]:
                maxI = i
        for i in range(s,maxI):
                profit += arr[maxI] - arr[i]
        s = maxI + 1
    print(f'#{tc} {profit}')

    #유라2
    # profit = 0
    # maxI = N-1
    # for i in range(N-2,-1,-1):
    #     if arr[maxI] < arr[i]:
    #         maxI = i
    #     else:
    #         profit += arr[maxI] - arr[i]
    # print(f'#{tc} {profit}')
    #

    # 실패....ㅜ
    # profit = 0
    # for i in range(N-1):
    #     max_v = arr[i]
    #     for j in range(1,N-i):
    #         if max_v < arr[i+j]:
    #             max_v = arr[i+j]
    #     profit += max_v-arr[i]
    # print(f'#{tc} {profit}')