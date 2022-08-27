from sys import stdin
import heapq

from math import inf
input = stdin.readline

# 연산의 개수
N = int(input())
# 양수 음수 따로 넣어서 각 리스트에서 절댓값이 가장 작은 것을 꺼내서 비교
plus = []
minus = []
# 연산의 정보
for _ in range(N):
    x = int(input())
    # 양수 리스트
    if x > 0:
        heapq.heappush(plus, x)
    # 음수 리스트
    elif x < 0:
        heapq.heappush(minus, -x)
    # 0
    else:
        p = inf
        m = inf
        # 비어있지 않을 때 pop가능
        if plus:
            p = heapq.heappop(plus)
        if minus:
            m = heapq.heappop(minus)
        # inf라는건 비어있다는 뜻
        if p == inf and m == inf:
            print(0)
        elif p >= m:
            print(-m)
            if p != inf:
                heapq.heappush(plus,p)
        else:
            print(p)
            if m != inf:
                heapq.heappush(minus,m)

import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    num =int(input())
    
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))