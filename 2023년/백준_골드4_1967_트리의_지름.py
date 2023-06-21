'''
    접근법
    
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 노드의 개수
n = int(input())
# 간선 edge[r] : r행에서 이동가능한 [번호, 가중치]
edge = [[] for _ in range(n)]

for _ in range(n-1):
    # 부모, 자식, 가중치
    s,e,v = map(int,input().split())
    edge[s-1].append([e-1,v])
    edge[e-1].append([s-1,v])
    
def dfs(i):
    # i에서 이동하기
    for e,v in edge[i]:
        # 방문한 적 x
        if visited[e] == 0:
            visited[e] = visited[i] + v
            dfs(e)    

# 0번 노드에서 가장 멀리 있는 노드(x) 찾기 
visited = [0] * n
visited[0] = 1
dfs(0)
x = visited.index(max(visited))

# x번 노드에서 가장 멀리 있는 노드(y) : x와 y의 거리 == 지름
visited = [0]*n
visited[x] = 1
dfs(x)

print(max(visited))