# BFS

너비우선탐색

탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정

점들을 차례로 방문하는 방식

한번에 한 칸씩 : 최단거리, 영역/조건 탐색 -> 미로/경로 찾기의 전형적 template 

선입선출



```
def BFS(G,v,n):                             # 그래프 G, 탐색 시작점 v
    visited = [0]*(n+1)                     # n : 정점의 개수
    queue = []                              # 큐 생성
    queue.append(v)                         # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:                            # 큐가 비어있지 않는 경우
        t = queue.pop(0)                    # 큐의 첫번째 원소 반환
        visit(t)                            # 정점 t에서 할일
        for i in G[t]:                      # t와 연결된 모든 정점에 대해
            if not visited[i]:              # 방문되지 않은 곳이라면
                queue.append(i)             # 큐에 넣기
                visited[i] = visited[t] + 1 # t으로부터 1만큼 이동 (v로부터 얼마나 떨어져 있는지 표시)
 
```

