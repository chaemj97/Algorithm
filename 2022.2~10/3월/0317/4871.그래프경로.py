# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 노드개수,간선개수
    V, E = map(int,input().split())
    # 인접 행렬
    adj = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        # 출발 도착
        s, e = map(int,input().split())
        adj[s][e] = 1
    # 출발노드, 도착노드 : 경로 존재하는가?
    S, G = map(int,input().split())

    # 방문여부 표시
    visited = [0] * (V+1)
    stack = []
    stack.append(S)
    visited[S] = 1
    # 기본값은 가는 길 존재 X
    result = 0
    while stack:
        top = stack[-1]
        # 도착?
        if top == G:
            result = 1
            break
        # 갈 수 있는 경로 다 찾기
        for i in range(V + 1):
            # 길이 있고, 방문한적 없는 곳이면 가자
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        # 길이 업다면 되돌아가기
        else:
            stack.pop()

    print(f'#{tc} {result}')