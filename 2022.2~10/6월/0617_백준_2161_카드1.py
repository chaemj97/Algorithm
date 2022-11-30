from sys import stdin
from collections import deque

# 카드 1~N번
N = int(stdin.readline())
cards = deque([i for i in range(1,N+1)])

answer = []
while cards:
    # 맨 위에 있는 카드 버리기
    answer += [cards.popleft()]
    # 맨 위에 있는 카드 맨 뒤로
    cards.rotate(-1)

print(*answer)