# https://chaemi720.tistory.com/201

from sys import stdin
from collections import deque
input = stdin.readline

F,S,G,U,D = map(int,input().split())
# 총 F층인 건물, S층에서 G층 가기

# 방문 표시
visited = [0]*(F+1)

# 최단 경로 구하는 것이니 bfs
def bfs(now):
    global visited
    visited[now] = 1

    que = deque()
    que.append(now)

    while que:
        # 현 위치
        c_floor = que.popleft()
        # 도착?
        if c_floor == G:
            return visited[c_floor]-1

        # 이동
        for i in [U,-D]:
            # 건물 층 수 내, 방문한 적 없는 층
            if 0 < c_floor + i <= F and visited[c_floor + i] == 0:
                que.append(c_floor + i) 
                visited[c_floor + i] = visited[c_floor] + 1
    # 도착 못했다면
    return 'use the stairs'

print(bfs(S))