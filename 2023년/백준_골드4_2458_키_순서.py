'''
    접근법
        목표
        : 나보다 키가 작은 사람수 + 나보다 키가 큰 사람 수가 n-1명인가?
'''
import sys
input = sys.stdin.readline

# 학생 수, 비교 횟수
n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b, = map(int,input().split())
    graph[a][b] = 1

# i -> j -> k
for j in range(1,n+1):
    for i in range(1,n+1):
        for k in range(1,n+1):
            if i != k:
                # i는 j보다 키가 작고 j는 k보다 키가 작다 == i는 k보다 키가 작다
                if graph[i][j] == 1 and graph[j][k] == 1:
                    graph[i][k] = 1
                    
answer = 0
for i in range(1,n+1):
    # i보다 작은 사람 수 + i보다 키 큰 사람 수
    cnt = 0
    for j in range(1,n+1):
        # graph[i][j] == 1 : i보다 키 크다
        # graph[j][i] == 1 : i보다 키 작다
        cnt += graph[i][j] + graph[j][i]
    # 자기 자신 말고 나머지 n-1개와의 상태를 아는가?
    if cnt == n-1:
        answer += 1
print(answer)