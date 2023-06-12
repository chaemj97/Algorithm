'''
    접근법
        시작방에서 끝방까지 지나는 검은 방의 개수가 최소!
        흰방만으로 다 탐색 후 목적지에 도달할 수 없다면 검은방 탐색하기
        -> 우선순위큐
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int,input().rstrip())) for _ in range(n)]

# 방문 여부
visited = [[0]*n for _ in range(n)]

# [지나간 검은색 방 개수, r, c]
heap = []
heapq.heappush(heap,[0,0,0])
visited[0][0] = 1

while heap:
    black_cnt,cr,cc = heapq.heappop(heap)
    # 도착?
    if cr == n-1 and cc == n-1:
        print(black_cnt)
        break
    # 이동
    for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
        nr = cr + dr
        nc = cc + dc
        # 범위 내 방문한 적 없다
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
            # 방문 표시
            visited[nr][nc] = 1
            # 흰색?
            if room[nr][nc] == 1:
                heapq.heappush(heap,[black_cnt,nr,nc])
            # 검은색?
            # 흰색 다 돌고 돌아야 하니 우선순위 뒤로 미루기
            else:
                heapq.heappush(heap,[black_cnt+1,nr,nc])