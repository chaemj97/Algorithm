#교수님
import sys
sys.stdin = open('sample_input.그래프.txt')
T = int(input())
for tc in range(1,T+1):
    # 노드개수,간선개수
    V, E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        # 출발 도착
        s, e = map(int,input().split())
        adj[s][e] = 1
    S, G = map(int,input().split())
    # S에서 dfs 수행
    # 방문여부 표시
    visited = [0]*(V+1)
    stack = []
    stack.append(S)
    visited[S] = 1
    # 여기서부터 dfs 수행
    result = 0
    while stack:
        top = stack[-1]
        # 경로 찾음
        if top == G:
            result = 1
            break
        # 갈 수 있는 경로 다 찾기
        for i in range(V+1):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    print(f'#{tc} {result}')