# 트리의 지름 : 노드 사이 거리가 가장 먼 경로
# 루트 == 1

import sys
sys.setrecursionlimit(10 ** 6)
# 노드의 개수
n = int(input())

# a행 : a행에서 이동가능한 [노드 번호, 가중치]
arr = [[] for _ in range(n)]

for _ in range(n-1):
    # 부모, 자식, 가중치
    s,e,v = map(int,input().split())
    arr[s-1].append([e-1,v])
    arr[e-1].append([s-1,v])

def dfs(s):
    # s에서 이동하기
    for e,v in arr[s]:
        # 방문한 적 없다면
        if visited[e] == -1:
            visited[e] = visited[s] + v
            dfs(e)

# 노드1에서 가장 멀리있는 노드 찾기
visited = [-1] * n
visited[0] = 0
dfs(0)
x = visited.index(max(visited))

# x에서 가장 멀리있는 노드 : 트리의 지름 양 끝 노드
visited = [-1] * n
visited[x] = 0
dfs(x)

print(max(visited))