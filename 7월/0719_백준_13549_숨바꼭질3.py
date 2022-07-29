from sys import stdin
from collections import deque
input = stdin.readline

# 수빈 위치, 동생 위치
N, K = map(int,input().split())

# 방문 표시
visited = [-1]*100001
visited[N] = 0

# bfs
que = deque()
que.append(N)

while que:
    # 현 위치
    current = que.popleft()
    # 도착?
    if current == K:
        break
    # 순간 이동 (범위 내, 방문 한 적 없음) -> 시간 0초
    if 0 < current*2 <= 100000 and visited[current*2] == -1:
        visited[current*2] = visited[current]
        # 맨 앞에 추가 -> 1칸씩 가는 것보다 빨리 도착
        que.appendleft(current*2)
    # 걷기
    for i in [1,-1]:
        # (범위 내, 방문 한 적 없음) -> 시간 1초
        if 0 <= current + i <= 100000 and visited[current+i] == -1:
            visited[current+i] = visited[current] + 1
            # 맨 뒤에 추가
            que.append(current+i)

# 결과
print(visited[K])