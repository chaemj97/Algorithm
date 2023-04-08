'''
    DFS : 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
    BFS : 가까운 노드부터 탐색하는 알고리즘
'''
from collections import deque
import sys
input = sys.stdin.readline

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
N,M,V = map(int,input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(N+1):
    edge[i].sort()

# DFS
def dfs(v):
    result = [v]
    stack = [v]
    visited = [0]*(N+1)
    visited[v] = 1
    while stack:
        c = stack[-1]
        for i in edge[c]:
            if visited[i] == 0:
                result.append(i)
                visited[i] = 1
                stack.append(i)
                break
        else:
            stack.pop()
    return result

# BFS
def bfs(v):
    result = [v]
    que = deque([v])
    visited = [0]*(N+1)
    visited[v] += 1
    while que:
        c = que.popleft()
        for i in edge[c]:
            if visited[i] == 0:
                result.append(i)
                que.append(i)
                visited[i] = 1
    return result                

print(*dfs(V))
print(*bfs(V))