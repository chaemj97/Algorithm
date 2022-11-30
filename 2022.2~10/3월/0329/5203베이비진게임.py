def baby_gin(play):
    check = [0]*10
    # 카드 숫자 세기
    for i in play:
        check[i] += 1

    # triplet
    if 3 in check:
        return True
    # run
    for i in range(8):
        if check[i] and check[i+1] and check[i+2]:
            return True

# 테스트케이스 개수
T = int(input())
for tc in range(1,T+1):
    card = list(map(int,input().split()))

    # 플레이어 1, 플레이어 2
    play1 = []
    play2 = []
    result = 0
    # 카드 3장이상일 때 baby_gin 확인
    for i in range(6):
        play1.append(card[i*2])
        if len(play1) >2 and baby_gin(play1):
            result = 1
            break
        play2.append(card[i*2+1])
        if len(play2) >2 and baby_gin(play2):
            result = 2
            break

    print(f'#{tc} {result}')
