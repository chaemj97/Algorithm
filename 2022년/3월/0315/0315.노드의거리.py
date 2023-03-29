# S에서 시작해서 G로 도착하는 최단거리 반환
def bfs(S,G):
    queue = []
    # result를 구하기 위해, 각 노드에서 몇번째 이동했는지 알아야 된다.
    queue.append((S,0))
    visited = [0]*(V+1)
    visited[S] = 1
    while queue:
        front,diestance = queue.pop(0) # 현재 노드
        if front == G: # 목적지에 도착했으니 종료

            return diestance
        # 현재 노드에서 갈 수 있는 경로 찾기
        for i in range(1,V+1):
            # 연결되어 있고 방문하지 않은 노드라면 방문
            if adj[front][i] and not visited[i]:
                queue.append((i,diestance+1))
                visited[i] = 1

    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for e in range(E):
        s,g = map(int,input().split())
        adj[s][g] = 1
        adj[g][s] = 1
    S,G = map(int, input().split())
    # bfs 수행
    print(f'#{tc} {bfs(S,G)}')