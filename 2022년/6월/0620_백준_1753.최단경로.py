# https://chaemi720.tistory.com/174

from sys import stdin,maxsize
# 최소힙
import heapq
# 정점의 개수, 간선의 개수
V, E = map(int,stdin.readline().split())
# 시작 정점 번호
K = int(stdin.readline())

# 인접 리스트, [비용, 도착 노드]
edge = [[] for _ in range(V+1)]

INF = maxsize
# K에서 최단 경로
dist = [INF] * (V+1)

# u에서 v로 가는 가중치 w
for _ in range(E):
    u,v,w = map(int,stdin.readline().split())
    edge[u].append([w,v])

# 시작점 초기화
dist[K] = 0
# [거리, 다음 노드]
heap = [[0,K]]

while heap:
    # 최소 힙
    w,v = heapq.heappop(heap)
    # v가 갱신되기 전 경로면 그냥 버리기
    if dist[v] != w:
        continue
    # v에서 갈 수 있는 노드 확인
    for nw, nv in edge[v]:
        # 이전 이동 거리보다 새로운 간선 거칠 때 더 최소거리면 갱신
        if dist[nv] > w + nw:
            dist[nv] = w + nw
            heapq.heappush(heap,[dist[nv],nv])

# 최단 경로값 출력
for i in range(1,V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])