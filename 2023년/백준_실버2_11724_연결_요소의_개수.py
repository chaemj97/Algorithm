'''
    접근법 1
        visited를 활용해 bfs로 검사

'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    global visited,edge
    visited[i] = 1
    que = deque()
    que.append(i)
    while que:
        c = que.popleft()
        for j in edge[c]:
            if visited[j] == 0:
                visited[j] = 1
                que.append(j)
    

N,M = map(int,input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
    
visited = [0]*(N)
answer = 0
for i in range(N):
    if visited[i] == 0:
        bfs(i)
        answer += 1
        
print(answer)