'''
    접근법
        bfs를 활용하여 이동하기
    
'''
from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

visited = [0]*100001
move = [0]*100001

# 잡은 경로 표시
def path(c):
    # 잡은 경로 거꾸로 표시
    answer = []
    for _ in range(visited[c]+1):
        answer.append(str(c))
        c = move[c]
    print(' '.join(answer[::-1]))
    
# 잡기
def bfs():
    que = deque()
    que.append(n)
    while que:
        # 현 위치
        c = que.popleft()
        # 잡았다?
        if c == k:
            # 걸린 시간
            print(visited[c])
            # 경로
            path(c)
            break
        # 이동
        for d in (c+1,c-1,c*2):
            # 범위 내, 방문한적 X
            if 0 <= d <= 100000 and visited[d] == 0:
                que.append(d)
                visited[d] = visited[c] + 1
                # c에서 d로 이동 표시
                move[d] = c
                
bfs()