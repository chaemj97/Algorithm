'''
    접근법
        deque를 이용해 이동
    
'''
from collections import deque
import sys
input = sys.stdin.readline

# 수빈, 동생
n,k = map(int,input().split())

visited = [-1 for _ in range(100001)]
que = deque()

visited[n] = 0
que.append(n)

while que:
    c = que.popleft() # 현 위치
    if c == k:
        print(visited[k])
        break
    if 0<= c-1 and visited[c-1] == -1:
        visited[c-1] = visited[c] + 1
        que.append(c-1)
        
    if c*2 <= 100000 and visited[c*2] == -1:
        que.append(c*2)
        visited[c*2] = visited[c]
        
    if c+1 <= 100000 and visited[c+1] == -1:
        visited[c+1] = visited[c] + 1
        que.append(c+1)
        
    