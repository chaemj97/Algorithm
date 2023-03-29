# https://chaemi720.tistory.com/157

from collections import deque
# N장의 카드, 카드 번호 1~N
N = int(input())
cards = [i for i in range(1,N+1)]
card = deque(cards)
while len(card) > 1:
    # 맨 윗장 버리기
    card.popleft()
    # 맨 윗장을 맨 뒤로 보내기
    card.rotate(-1)
print(card[0])
    