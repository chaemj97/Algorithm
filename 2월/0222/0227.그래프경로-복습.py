import sys
sys.stdin = open('sample_input.그래프.txt')

# 테스트 케이스의 개수
T = int(input())
for tc in range(1,T+1):
    # 노드개수,간선개수
    V, E = map(int,input().split())
    # 인접 행렬
    adj = [[0]*(V+1) for _ in range(V+1)]
    # E개의 출발 도착 노드 간선 정보
    for i in range(E):
        # 출발 도착
        s, e = map(int,input().split())
        adj[s][e] = 1
    # 경로의 존재를 확인할 출발 노드 S와 도착노드 G
    # 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력
    S, G = map(int,input().split())

    stack = []
    stack.append(S)
    visited = [0] * (V+1)
    visited[S] = 1
    # DFS 시작
    result = 0
    while stack:
        top = stack[-1]
        # 도착?
        if top == G:
            result = 1
            break
        # 아니면 경로 찾기
        for i in range(V+1):
            # 인접하고 방문한적 없으면 -> 방문
            if adj[top][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        # 이동할 곳이 없다면 되돌아 가기
        else:
            stack.pop()
    print(f'#{tc} {result}')

