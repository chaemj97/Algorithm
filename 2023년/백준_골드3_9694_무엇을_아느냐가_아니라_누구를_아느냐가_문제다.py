'''
    접근법
        0번에서 m-1번까지 최단 거리 구하는 문제
        다익스트라
'''
import heapq
import sys
input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())
for t in range(1,T+1):
    # 관계의 수, 정치인의 수
    n,m = map(int,input().split())
    # 관계 표시
    f = [[] for _ in range(m)]
    for _ in range(n):
        # 정치인, 그의 친구, 친밀도
        x,y,z = map(int,input().split())
        f[x].append([y,z])
        f[y].append([x,z])
    
    # 연결 경로
    path = [[] for _ in range(m)]
    # 친밀도
    dist = [float('inf') for _ in range(m)]
    
    # 0번에서 m-1번까지 최소 경로 구하기
    path[0] = [0]
    dist[0] = 0
    
    heap = []
    heapq.heappush(heap,[0,0])
    while heap:
        d,now = heapq.heappop(heap)
        # 이전에 now의 최소 경로가 바뀌었다면 pass
        if dist[now] != d:
            continue
        
        # now에서 이동해보기
        for next,next_d in f[now]:
            n = d + next_d
            # next까지 가는데 now를 거치는 것 / 거치지 않는 것 중 최소 선택
            if n < dist[next]:
                path[next] = path[now] + [next]
                dist[next] = n
                heapq.heappush(heap,[n,next])
    
    # print(dist)
    # print(path[m-1])
    
    print(f'Case #{t}: ',end='')
    # m-1번까지 도달 가능?
    if dist[m-1] != float('inf'):
        print(*path[m-1])
    else:
        print(-1)