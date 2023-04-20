'''
    접근법 1
        1. 내가 얼리어답터가 아니다
            내 자식들은 다 얼리어답터
        2. 내가 얼리어답터다
            내 자식들 상관 없음
        깊이 우선 탐색
        예제 확인 순서)
            5,6,2,3,7,8,4,1

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

# 사람 수
N = int(input())
# 친구 인접 리스트
friend = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
    
# [내가 얼리어답터인 경우, 내가 얼리어답터가 아닌 경우]
dp = [[0,1] for _ in range(N+1)]
# 확인 여부
visited = [0]*(N+1)

def check(me):
    global visited
    visited[me] = 1
    # 내 친구들 확인
    for f in friend[me]:
        # 확인한 적 없는 친구
        if visited[f] == 0:
            check(f)
            # 내가 얼리어답터인 경우 
                # -> 친구가 얼리어답터든 아니든 상관 없다
                # -> 더 적은 경우 체크
            dp[me][1] += min(dp[f][0],dp[f][1])
            # 내가 얼리어답터가 아니다
                # -> 친구가 무조건 얼리어답터
            dp[me][0] += dp[f][1]

# 1번부터 깊이 우선 탐색        
check(1)

print(min(dp[1][0],dp[1][1]))