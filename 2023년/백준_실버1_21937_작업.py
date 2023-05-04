'''
    접근법 1
        x와 연결된 노드 개수 세기
'''
from collections import deque
import sys
input = sys.stdin.readline

# 작업 개수, 작업 순서 정보 개수
n,m = map(int,input().split())
order = [[] for _ in range(n+1)]

for _ in range(m):
    # a 다음에 b 일하기
    a,b = map(int,input().split())
    order[b].append(a)
# 오늘 반드시 끝내야하는 작업
x = int(input())

visited = [0]*(n+1)
visited[x] = 1
que = deque()
que.append(x)
answer = 0
while que:
    answer += 1
    c = que.popleft()
    # c 이전에 해야 할 작업들
    for d in order[c]:
        if visited[d] == 0:
            visited[d] = 1
            que.append(d)
# 작업 개수에서 자기 자신 빼기
print(answer-1)