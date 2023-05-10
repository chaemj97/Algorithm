'''
    접근법
        시간 제한 5초
        bfs를 활용해 각 시작점에 따라 몇개 해킹 가능한지 세기
    
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

trust = [[] for _ in range(n+1)]
for _ in range(m):
    # a가 b를 신뢰 == b를 해킹하면 a도 해킹 가능
    a,b = map(int,input().split())
    trust[b].append(a)
    
# start를 해킹하면 총 몇개 해킹 가능한가
def bfs(start):
    que = deque()
    que.append(start)
    visited = [0]*(n+1)
    visited[start] = 1
    cnt = 0
    while que:
        cnt += 1
        c = que.popleft()
        for i in trust[c]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1
    return cnt

# 각각 해킹 가능한 수 세기
answer = [[i,bfs(i)] for i in range(1,n+1)]
answer.sort(key=lambda x: -x[1])

# 가장 많은 해킹 수
max_answer = answer[0][1]
for j in range(n):
    if answer[j][1] == max_answer:
        print(answer[j][0],end=' ')
    else:
        break