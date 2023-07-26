'''
    접근법
        dfs로 방문 확인
    
'''
import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]

answer = 0
def dfs(cr,cc,cnt):
    global answer
    # 도착?
    if cr == 0 and cc == c-1:
        if cnt == k:
            answer += 1
        return 
    
    # 이동
    for dr, dc in [[-1,0],[1,0],[0,1],[0,-1]]:
        nr = cr + dr
        nc = cc + dc
        # 범위 내
        if 0 <= nr < r and 0 <= nc < c:
            # 방문 가능
            if arr[nr][nc] != 'T' and cnt+1 <= k:
                # 방문 처리
                arr[nr][nc] = 'T'
                dfs(nr,nc,cnt+1)
                # 되돌리기
                arr[nr][nc] = '.'

# 시작점 방문 
arr[r-1][0] = 'T'
dfs(r-1,0,1)
print(answer)