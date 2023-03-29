def nomal(r,c):
    global area1
    area1 += 1
    stack = []
    stack.append((r,c))
    used1[r][c] = 1
    while stack:
        # 현 위치
        cr,cc = stack[-1]
        # 4방향 확인
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr = cr+dr
            nc = cc+dc
            # 구역 내, 사용한적 X, 기준이랑 같으면
            if 0<=nr<N and 0<=nc<N and not used1[nr][nc] and arr[r][c] == arr[nr][nc]:
                used1[nr][nc] = 1
                stack.append((nr,nc))
                break
        # 4방향 다 갈 수 없다면 한 칸 되돌아 가기
        else:
            stack.pop()
def rg(r,c):
    global area2
    area2 += 1
    if arr[r][c] == 'B':
        s = 'B'
    else:
        s = 'RG'
    stack = []
    stack.append((r,c))
    used2[r][c] = 1
    while stack:
        cr,cc = stack[-1]
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr = cr+dr
            nc = cc+dc
            # 구역 내, 사용한적 X, 기준이랑 같으면(적록색약은 R과 G 같은 취급)
            if 0<=nr<N and 0<=nc<N and not used2[nr][nc] and arr[nr][nc] in s:
                used2[nr][nc] = 1
                stack.append((nr,nc))
                break
        else:
            stack.pop()
# N*N 그리드
N = int(input())
# 그림
arr = [list(input()) for _ in range(N)]

# 적록색약이 아닌 사람
# 구역 체크한 곳 표시
used1 = [[0]*N for _ in range(N)]

area1 = 0
for r in range(N):
    for c in range(N):
        if not used1[r][c]:
            nomal(r,c)

# 적록색약
used2 = [[0]*N for _ in range(N)]
area2 = 0
for r in range(N):
    for c in range(N):
        if not used2[r][c]:
            rg(r,c)
print(area1,area2)