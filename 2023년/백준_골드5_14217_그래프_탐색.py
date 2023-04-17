'''
    접근법 1
        도로를 인접리스트로 만들기
        도로가 생성되거나 삭제될 때마다 bfs로 1번 도시와의 거리 체크

'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 각 도시별로 수도를 방문하는 데 최소 방문 도시
    visited = [-1]*(n+1)
    visited[1] = 0
    que = deque()
    que.append(1)
    while que:
        # 현재 위치
        c = que.popleft()
        # 이동
        for d in load[c]:
            if visited[d] == -1:
                visited[d] = visited[c]+1
                que.append(d)
    return visited[1:]

# 도시의 개수, 도로의 개수
n,m = map(int,input().split())
# 도로
load = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    load[x].append(y)
    load[y].append(x)

# 도로 정비 계획 도로 수
q = int(input())
for _ in range(q):
    a,i,j = map(int,input().split())
    # 도로 생성
    if a == 1:
        load[i].append(j)
        load[j].append(i)
    # 도로 삭제
    else:
        load[i].remove(j)
        load[j].remove(i)
    
    # 도시별 수도 방문 최소 방문 도시 수 구하기
    result = bfs()
    print(*result)