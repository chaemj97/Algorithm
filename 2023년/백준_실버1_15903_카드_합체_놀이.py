'''
    접근법
        제일 작은 두 수 합하기
        1. 리스트
        2. heapq
    
'''

import sys
input = sys.stdin.readline

# 카드의 개수, 합체 횟수
n,m = map(int,input().split())
card = list(map(int,input().split()))

# 리스트
'''
for _ in range(m):
    # 정렬 후 제일 작은 두 수 합하기
    card.sort()
    new = card[0] + card[1]
    card[0] = new
    card[1] = new
'''

# heap
import heapq
heapq.heapify(card)
for _ in range(m):
    # 제일 작은 두 수
    one = heapq.heappop(card)
    two = heapq.heappop(card)
    # 합해서 다시 넣기
    heapq.heappush(card,one+two)
    heapq.heappush(card,one+two)
print(sum(card))