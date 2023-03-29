from sys import stdin
input = stdin.readline

# 정점의 개수
N = int(input())
# 인접 행렬
adj = [list(map(int,input().split())) for _ in range(N)]

# a -> b and b -> c == a -> c
for b in range(N):
    for a in range(N):
        for c in range(N):
            if adj[a][b] and adj[b][c]:
                adj[a][c] = 1

# 결과 출력
for i in range(N):
    print(*adj[i])