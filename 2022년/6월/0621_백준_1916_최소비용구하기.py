# https://chaemi720.tistory.com/177

from sys import stdin, maxsize
import heapq

input = stdin.readline

# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())

money = [[] for _ in range(N+1)]
for _ in range(M):
    # 출발 도시, 도착 도시, 버스 비용
    s,e,m = map(int,input().split())
    money[s].append([m,e])

# start에서 end까지 최소 비용 구하기
start, end = map(int, input().split())

INF = maxsize
dist = [INF] * (N+1)
# 시작점은 비용 0
dist[start] = 0
# [비용, 다음 도시]
heap = [[0,start]]

while heap:
    # 비용이 최소인거 pop (최소힙)
    m,e = heapq.heappop(heap)
    # e로 가는 비용이 최소비용으로 갱신된 후 값이면 버리기
    if dist[e] != m:
        continue
    # e에서 이동해보자
    for nm,ne in money[e]:
        # 이전 이동 거리보다 e를 거칠 때 더 최소 비용이면 갱신
        if dist[ne] > m + nm:
            dist[ne] = m + nm
            heapq.heappush(heap, [dist[ne], ne])

# end 도착 최소 비용은?
print(dist[end])