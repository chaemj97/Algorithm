import heapq

# 정점의 개수, 간선리스트의 간선 수
n, m = map(int,input().split())
edge = [[] for _ in range(n+1)]

# 간선 정보
for __ in range(m):
    a,b,c = map(int,input().split())
    edge[a].append((c,b))
    edge[b].append((c,a))

# 두 정점이 연결되는 시점의 간선의 가중치 합의 최솟값 구하기
s, t = map(int,input().split())

INF = float('inf')
# s에서 거리
dist = [INF]*(n+1)
# 시작점 초기화
dist[s] = 0
# [가중치, 다음 노드]
heap = [[0,s]]

while heap:
    # 최소 힙
    value,now = heapq.heappop(heap)
    # 이미 now가 갱신되었다면 패쓰!!!
    if dist[now] != value:
        continue
    # 이동해보자
    for next_value, next in edge[now]:
        # 새로운 간선을 거치는게 최소인가?
        if dist[next] > value + next_value:
            dist[next] = value + next_value
            heapq.heappush(heap,[dist[next],next])

print(dist[t])