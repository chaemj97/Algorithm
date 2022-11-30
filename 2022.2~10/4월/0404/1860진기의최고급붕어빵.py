# 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # N명의 손님, M초동안 K개 붕어빵
    N,M,K = map(int,input().split())
    # 각 사람이 언제 도착하는지
    time = list(map(int,input().split()))
    # 오름차순 정리
    time.sort()

    # 기본값 : 가능하다
    result = 'Possible'

    # 손님이 도착할 시간에 몇개의 빵이 있는가?
    # 빵의 개수(bread)보다 손님의 수(i+1)가 적어야 가능
    for i in range(N):
        bread = time[i]//M*K
        if bread < i+1:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')