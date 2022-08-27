from collections import deque

# 입력한 x에 따라 셔플을 진행하는 함수
def shuffle(x,cards):
    result = []

    if x < N//2:
        L = deque(cards[:N//2])
        R = deque(cards[N//2:])

        num = N//2 - x

    else:
        L = deque(cards[N//2:])
        R = deque(cards[:N//2])

        num = x - (N//2)+1

    for _ in range(num):
        result.append(L.popleft())
    
    while len(R) > num:
        result.append(R.popleft())
        result.append(L.popleft())

    while R:
        result.append(R.popleft())
         
    return result

# 카드를 셔플시키고, 횟수를 계산하는 함수
def mixed(cnt,cards):
    global answer

    # 최소 횟수가 아니거나 5 이상인경우 실패    
    if cnt >= answer or cnt > 5:
        return

    # 3. 카드가 정렬되어 있는지 확인
    if cards == sort_cards or cards == r_sort_cards:
        answer = min(answer,cnt)
        return

    # 0부터 시작할 필요가 없음, 0은 카드 배열 그대로
    for i in range(1,N):
        mixed(cnt+1,shuffle(i,cards))

# 1. 입력
T = int(input())
for tc in range(1,T+1):
    # 카드 갯수
    N = int(input())
    cards = list(map(int,input().split()))

    sort_cards = sorted(cards)
    r_sort_cards = sorted(cards,reverse=True)

    answer = float('inf')

    # 2. 셔플 진행
    mixed(0,cards)

    if answer > 5:
        answer = -1

    print(f'#{tc} {answer}')