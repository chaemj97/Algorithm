'''
    접근법
        bfs를 이용해 최소 경우 구하기
    
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m,a,b = map(int,input().split())

limit = [0]*(n+1)
for _ in range(m):
    i,j = map(int,input().split())
    for k in range(i,j+1):
        limit[k] = 1

que = deque()
que.append(0)
flag = False
visited = [0]*(n+1)
while que:
    c = que.popleft()
    if c == n:
        flag = True
        break
    for d in [a,b]:
        if c+d <= n and visited[c+d] == 0 and limit[c+d] == 0:
            visited[c+d] = visited[c] + 1
            que.append(c+d)

if flag:
    print(visited[n])
else:
    print(-1)