import heapq 
import sys
input = sys.stdin.readline

heap = []

# 연산의 개수
N = int(input())

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap,x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
