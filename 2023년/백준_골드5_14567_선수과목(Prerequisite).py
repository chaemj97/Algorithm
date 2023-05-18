'''
    접근법
        순서 조건이 주어졌을 때 전체 순서 보기
        -> 위상정렬
'''
from collections import deque
import sys
input = sys.stdin.readline

# 과목의 수, 선수 조건의 수
n,m = map(int,input().split())
# 선수과목 수
front_cnt = [0]*(n+1)
# 다음에 들을 과목
back_subject = [[] for _ in range(n+1)]
# 선수 조건
for _ in range(m):
    # a 다음에 b 듣기
    a,b = map(int,input().split())
    front_cnt[b] += 1
    back_subject[a].append(b)
    
answer = [0]*(n+1)
que = deque()
# 선수 과목이 없는 과목부터 듣기
for i in range(1,n+1):
    if front_cnt[i] == 0:
        answer[i] = 1
        que.append(i)
        
while que:
    c = que.popleft()
    # c 다음에 들을 과목들
    for next in back_subject[c]:
        front_cnt[next] -= 1
        # 선수 과목들을 다 들었는가?
        if front_cnt[next] == 0:
            answer[next] = answer[c] + 1
            que.append(next)

print(*answer[1:])