import sys
sys.stdin = open('sample_input.퍼펙트셔플.txt')

# 테스트 케이스의 개수
T = int(input())
for tc in range(1,T+1):
    # N장의 카드
    N = int(input())
    card = input().split()

    result = ['']*len(card)
    # 홀수 장
    if N%2:
        for i in range(N//2+1):
            result[2*i] = card[i]
        for i in range(N//2):
            result[2*i+1] = card[i+N//2+1]
    # 짝수 장
    else:
        for i in range(N//2):
            result[2*i] = card[i]
            result[2*i+1] = card[i+N//2]

    print(f'#{tc}',*result)

    # 교수님

    # if N%2:
    #     idx2 = N//2+1
    # else:
    #     idx2 = N//2
    # idx2 = (N+1)//2

    # 참조1 n = 0=>1=>=>3=>0
    # n += 1
    # if n+1 == 4:
    #     n = 0
    # n = (n+1)%4

    # # 참조 2 0=>1, 1=>0
    # if n == 1:
    #     n = 0
    # else:
    #     n = 1
    # n = (n+1)%2

    st_idx1 = 0
    st_idx2 = (N+1)//2
    print(f'#{tc}',end=' ')
    for i in range(st_idx2):
        print(card[st_idx1+i],end=' ')
        if st_idx2+i < N:
            print(card[st_idx2+i],end=' ')
    print()
