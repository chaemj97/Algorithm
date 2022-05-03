# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # N개의 카드
    N = int(input())
    card = input().split()

    # 결과
    result = [0]*N
    for i in range((N+1)//2):
        try:
            # 앞쪽 카드
            result[i*2] = card[i]
            # 뒤쪽 카드
            result[i*2+1] = card[i+(N+1)//2]
        except:
            # 홀수장일 때 마지막 카드 없으니 오류
            continue
    print(f'#{tc}',*result)