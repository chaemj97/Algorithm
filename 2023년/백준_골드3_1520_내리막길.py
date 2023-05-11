'''
    접근법
        시작 지점에서 출발해서 DP 테이블이 갱신되지 않은 곳(X)을 만난다면
            해당 지점(X)부터 도착 지점까지 갈 수 있는 경로의 수를 그곳에 업데이트
         X지점의 DP 테이블이 이미 갱신되어 있다면 
            그 곳이 위에서 말한 부분 최적해가 되므로 그 값을 그대로 전체 정답에 더하기
'''
import sys
input = sys.stdin.readline

# 지도 크기
m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

dp = [[-1]*n for _ in range(m)]

def dfs(r,c):
    # 도착지점에 도착?
    if r == m-1 and c == n-1:
        return 1
    
    # 이미 방문한 적 있는가?
    if dp[r][c] != -1:
        return dp[r][c]
    
    # (r,c)에서 (m-1,n-1)까지 갈 수 있는 방법 수
    cnt = 0
    # 4방향 확인
    for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
        nr = r + dr
        nc = c + dc
        # 범위 내 + 이동 가능
        if 0<=nr<m and 0<=nc<n and arr[r][c] > arr[nr][nc]:
           cnt += dfs(nr,nc)
    dp[r][c] = cnt
    return cnt

# 결과
print(dfs(0,0))