# 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # N : 예약손님수, M초의 시간동안 K개 만들 수 있음
    N,M,K = map(int,input().split())
    # 사람이 언제 도착하는지를 초 단위로 나타냄
    guests = list(map(int,input().split()))
    # 손님 오는 순서 정리
    guests.sort()
    result = 'Possible'
    for i in range(N):
        # t초에 몇개의 빵이 안들어지는지 : 계산식을 구한다
        t = guests[i]//M * K
        # 내 앞에 있는 사람 수보다 빵이 많아야 나도 받을 수 있다
        # 나도 받아야함
        if t < (i+1):
            result = 'Impossible'
            break
    print(f'#{tc} {result}')