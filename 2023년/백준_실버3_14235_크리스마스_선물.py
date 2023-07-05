'''
    접근법
        heapq를 사용
        heapq.heappush 할 때 값에 -붙이면 가장 가치 있는 선물을 구할 수 있다.
    
'''
import heapq
import sys
input = sys.stdin.readline

# 방문 횟수
n = int(input())

gift = []
for _ in range(n):
    a = list(map(int,input().split()))
    # 아이들 만남
    if a[0] == 0:
        # 줄 수 있는 선물 중 가치 높은 것
        if len(gift) > 0:
            print(-heapq.heappop(gift))
        # 가지고 있는 선물이 없다.
        else:
            print(-1)
    # 선물 충전
    # [선물 개수, 선물 정보]
    else:
        for i in range(1,len(a)):
            heapq.heappush(gift,-a[i])
