'''
    접근법
        v를 본 소에게 추천할 연결관계 k 이상 동영상 개수 구하기
        그 경로의 모든 연결들의 USADO 중 최솟값
        → deque 활용
    
'''
from collections import deque
import sys
input = sys.stdin.readline

# 동영상 수, 질문 수
n,q = map(int,input().split())
# 동영상 쌍
usado = [[] for _ in range(n+1)]
for _ in range(n-1):
    # a와 b가 r로 연결
    a,b,r = map(int,input().split())
    usado[a].append((b,r))
    usado[b].append((a,r))
    
# 질문
for _ in range(q):
    # v를 본 소에게 추천할 연결관계 k 이상 동영상 개수
    k,v = map(int,input().split())
    
    # 확인 여부
    visited = [0]*(n+1)
    visited[v] = 1
    
    que = deque()
    que.append((v,float('inf')))
    
    cnt = 0
    
    while que:
        v,r = que.popleft()
        for next_v,next_r in usado[v]:
            next_r = min(r,next_r)
            # k이상? + 확인한 적 없음
            if next_r >= k and visited[next_v] == 0:
                cnt += 1
                visited[next_v] = 1
                que.append((next_v,next_r))
    print(cnt)