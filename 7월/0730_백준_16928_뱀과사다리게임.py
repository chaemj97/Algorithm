from sys import stdin
from collections import deque
input = stdin.readline

# 사다리 수, 뱀의 수
N, M = map(int, input().split())

game = [i for i in range(101)]
visited = [0]*101
visited[1] = 1

# 사다리 정보
for _ in range(N):
    x, y = map(int, input().split())
    game[x] = y

# 뱀의 정보
for _ in range(M):
    u, v = map(int, input().split())
    game[u] = v

que = deque()
que.append(1)
while que:
    current = que.popleft()
    for i in range(6,0,-1):
        # 범위 내에 있고 방문한 적 없다면
        if current + i <= 100 and visited[game[current + i]] == 0:
            # 방문 표시
            visited[game[current+i]] = visited[current] + 1
            if game[current+i] == 100:
                print(visited[100]-1)
                exit(0)
            que.append(game[current+i])
