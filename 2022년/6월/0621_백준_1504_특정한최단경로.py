# https://chaemi720.tistory.com/175

from sys import stdin,maxsize
import heapq
input = stdin.readline

# 정점의 개수, 간선의 개수
N, E = map(int,input().split())

edge = [[] for _ in range(N+1)]
for _ in range(E):
    # a에서 b까지 거리 c
    a,b,c = map(int,input().split())
    # 방향성이 없음
    # [거리, 도착 정점]
    edge[a].append([c,b])
    edge[b].append([c,a])

# 무조건 지나야 하는 2점
v1,v2 = map(int,input().split())

INF = maxsize

def dijkstra(start):
    dist = [INF]*(N+1)
    # 시작점은 거리가 0
    dist[start] = 0
    heap = [[0,start]]

    while heap:
        # 거리가 가장 짧은 걸로 pop
        # 거리, 도착 정점
        d,e = heapq.heappop(heap)
        # e로 가는 거리가 최단경로로 갱신된 후 값이면 버리기
        if dist[e] != d:
            continue
        # e에서 이동해보자
        for nd,ne in edge[e]:
            # e를 거쳐가는게 더 최단 경로면 갱신
            if dist[ne] > d + nd:
                dist[ne] = d + nd
                heapq.heappush(heap,[dist[ne],ne])
    return dist

# 1, v1, v2에서 각각 출발
one_start = dijkstra(1)
v1_start = dijkstra(v1)
v2_start = dijkstra(v2)
# 1 -> v1 -> v2 -> N
gogo_1_2 = one_start[v1] + v1_start[v2] + v2_start[N]
# 1 -> v2 -> v1 -> N
gogo_2_1 = one_start[v2] + v2_start[v1] + v1_start[N]
result = min(gogo_1_2,gogo_2_1)

# 경로가 없다면 -1
if result >= INF:
    print(-1)
# 경로가 있다면 최단 경로 출력
else:
    print(result)