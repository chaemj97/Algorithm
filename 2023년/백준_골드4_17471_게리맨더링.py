'''
    접근법
        1번 구역이 k개면 2번 구역 n-k개
        각 구역이 연결되어있다면 각 구역의 합의 절댓값 차 구하기
    
'''
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

# 구역의 개수
n = int(input())
# 구역의 인구
people = list(map(int,input().split()))
# 인접리스트
adj = [[] for _ in range(n)]

# 인접한 구역
for i in range(n):
    arr = list(map(int,input().split()))
    for j in arr[1:]:
        adj[i].append(j-1)

# 구역 내에 사람들이 다 연결되어있는지 확인하기
def bfs(l):
    start = l[0]
    que = deque()
    que.append(start)
    # 방문 확인한 구역
    visited = set([start])
    # 구역 내 합
    l_s = 0
    while que:
        # 현 위치
        c = que.popleft()
        l_s += people[c]
        # 이동
        for i in adj[c]:
            # 확인한 적 X, 현 구역 내 존재
            if i not in visited and i in l:
                que.append(i)
                visited.add(i)
                
    # 구역 내 모두 연결?
    if len(l) == len(visited):
        return True, l_s
    else:
        return False, 0
            

answer = float('inf')
# 1번 구역 인원 == k
# 2번 구역 인원 == n - k
for k in range(1,n//2+1):
    # 1번 구역
    ones = list(combinations(range(n),k))
    for one in ones:
        # 1번 구역끼리 연결 되었는지 / 1번 구역 합
        connect1, s1 = bfs(one)
        # 2번 구역끼리 연결 되었는지 / 2번 구역 합
        connect2, s2 = bfs([i for i in range(n) if i not in one])
        
        # 두 구역 다 연결되어있다?
        if connect1 and connect2:
            answer = min(answer, abs(s1-s2))

# 결과 출력
if answer == float('inf'):
    print(-1)
else:
    print(answer)
                    
    
