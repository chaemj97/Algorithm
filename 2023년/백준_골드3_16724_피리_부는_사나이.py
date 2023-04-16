'''
    접근법 1
        사이클이 몇개인가?
        
'''

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
d = {'D' : [1,0],'L':[0,-1],'R':[0,1],'U':[-1,0]}

visited = [[0]*M for _ in range(N)]

def move(r,c,cycle):
    global answer
    # 방문한 적 있다.
    if visited[r][c] != 0:
        # 사이클인가?
        if visited[r][c] == cycle:
            answer += 1
        return
    
    # 방문한 적 없다
    else:
        visited[r][c] = cycle
        # 이동방향
        dr,dc = d[arr[r][c]]
        move(r+dr,c+dc,cycle)
    
# 사이클 번호
cycle = 1
answer = 0
for r in range(N):
    for c in range(M):
        move(r,c,cycle)
        cycle += 1
        
print(answer)