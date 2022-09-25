from pprint import pprint

# 테스트 케이스 
T = int(input())
for tc in range(1,T+1):
    # 가로, 세로,배추 위치의 개수
    M, N, K = map(int,input().split())

    # 땅
    baechu = []
    arr = [[0]*N for _ in range(M)]
    for __ in range(K):
        # 배추 위치
        x,y = map(int,input().split())
        arr[x][y] = 1
        baechu.append([x,y])

    answer = 0
    for cr,cc in baechu:
        # 나눠진 구역?
        if arr[cr][cc] == 1:
            answer += 1
            stack = [[cr,cc]]
            arr[cr][cc] = -1
            while stack:
                r,c = stack.pop()
                for dr,dc in [[-1,0],[0,1],[1,0],[0,-1]]:
                    nr = r + dr
                    nc = c + dc            
                    if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 1:
                        arr[nr][nc] = -1
                        stack.append([nr,nc])

    print(answer)