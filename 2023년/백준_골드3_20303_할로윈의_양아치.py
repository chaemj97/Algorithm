'''
    접근법
        https://chaemi720.tistory.com/311
'''
from collections import deque
import sys
input = sys.stdin.readline

# 아이들 수, 친구 관꼐수, 울음소리 제한
n,m,k = map(int,input().split())
candy = [0] + list(map(int,input().split()))

# 친구 관계
friend = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
    
# 연결된 아이들 그룹으로 묶기
def connect(x):
    # x번 아이와 연결된 친구들
    x_friend = 1
    # x번 아이가 속한 그룹의 총 사탕 수
    x_candy = candy[x]
    que = deque()
    que.append(x)
    checked[x] = 1
    while que:
        now = que.popleft()
        # now의 친구들
        for i in friend[now]:
            if checked[i] == 0:
                que.append(i)
                checked[i] = 1
                x_friend += 1
                x_candy += candy[i]
    return [x_friend,x_candy]
    
    
# [이 그룹의 아이들 수, 이 그룹의 총 사탕 수]
child_group = []
# 연결 확인 여부
checked = [0]*(n+1)
for i in range(1,n+1):
    # 확인한 적 없는 아이면 연결된 친구들 확인하기
    if checked[i] == 0:
        child_group.append(connect(i))

dp = [0 for _ in range(k+1)]
# 각 그룹을 뺏을지 말지 정하기
for i in range(len(child_group)):
    # 이 그룹의 아이들 수, 이 그룹의 총 사탕 수
    child_cnt,candy_cnt = child_group[i]
    for j in range(k,child_cnt-1,-1):
        # 이 그룹 뺏기/안 뺏기 더 좋은 거 선택
        dp[j] = max(dp[j-child_cnt]+candy_cnt, dp[j])

print(dp[k-1])