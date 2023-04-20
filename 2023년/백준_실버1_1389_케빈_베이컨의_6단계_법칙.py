'''
    접근법 1
        N이 최대 100이니 플로이드 가능 → O(N**3)
        모든 유저에서 모든 유저까지 최단 거리 구하기

'''

import sys
input = sys.stdin.readline

# 유저의 수, 친구 관계의 수
N, M = map(int,input().split())
friend = [[float('inf')]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    friend[a][b] = 1
    friend[b][a] = 1
for r in range(N+1):
    friend[r][r] = 0
    

# i와 j는 몇단계 친구인가?
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j:
                friend[i][j] = min(friend[i][j],friend[i][k]+friend[k][j])
                
answer = 0
f_sum = float('inf')
for i in range(1,N+1):
    if sum(friend[i][1:]) < f_sum:
        answer = i
        f_sum = sum(friend[i][1:])
print(answer)
    
