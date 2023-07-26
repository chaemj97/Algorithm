'''
    접근법
        한 칸씩 이동하면서 부메랑 추가 or 그냥 이동
        2가지 경우 모두 확인
        
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

# 0 0 | 0   | 0 0 |   0 
# 0   | 0 0 |   0 | 0 0
d = [[1,0,0,1],[-1,0,0,1],[0,-1,1,0],[-1,0,0,-1]]

answer = 0
# (r,c) : 현위치
# s : 현재까지 합
def dfs(r,c,s):
    global answer
    if c == m:
        c = 0
        r += 1
    # 탐색 끝
    if r == n:
        answer = max(answer,s)
        return
    # 부메랑 만들기 4가지
    if visited[r][c] == 0:
        for i in range(4):
            r1,c1 = r+d[i][0],c+d[i][1]
            r2,c2 = r+d[i][2],c+d[i][3]
            # 범위 내
            if 0<=r1<n and 0<=c1<m and 0<=r2<n and 0<=c2<m:
                # 부메랑 만든 적X
                if visited[r1][c1] == 0 and visited[r2][c2] == 0:
                    # 부메랑 만들기
                    visited[r][c] = 1
                    visited[r1][c1] = 1
                    visited[r2][c2] = 1
                    dfs(r,c+1,s+arr[r][c]*2+arr[r1][c1]+arr[r2][c2])
                    # 되돌리기
                    visited[r][c] = 0
                    visited[r1][c1] = 0
                    visited[r2][c2] = 0
    # 다음 칸
    dfs(r,c+1,s)
        
dfs(0,0,0)
# 결과 출력
print(answer)