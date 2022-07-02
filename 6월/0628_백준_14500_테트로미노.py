

from sys import stdin
input = stdin.readline

# 세로, 가로
N, M = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(N)]

# 테트로미노 만들기
# 현 위치(r, c), 현재까지 합(s), 정사각형 갯수(cnt), 현재 테트로미노 조각 위치(used)
def check(r, c, s, cnt, used):
    global max_sum
    # 정사각형 수가 4개? == 완성
    if cnt == 4:
        # 합이 최대?
        max_sum = max(max_sum,s)
        return
    # 테트로미노 만들기
    for dr, dc in [[-1,0],[1,0],[0,1]]:
        nr = r + dr
        nc = c + dc
        # 종이 안에 있고, 사용한 적 없는 정사각형이라면 -> 테트로미노의 조각 
        if 0 <= nr < N and 0 <= nc < M and (nr,nc) not in used:
            # ㅗ 모양 만들기
            if cnt == 3:
                # 가로로 3개 연속인가?
                if used[0][1]==used[1][1]==used[2][1]:
                    for y in [-1,1]:
                        # 중간에 튀어나온 부분
                        cr = used[1][0]
                        cc = used[1][1] + y
                        # 종이 안에 있는가
                        if 0 <= cc < M:
                            check(cr, cc, s+paper[cr][cc], cnt+1, used+[(cr,cc)])
                # 세로로 3개 연속인가?
                elif used[0][0]==used[1][0]==used[2][0]:
                    for x in [-1,1]:
                        # 중간에 튀어나온 부분
                        cr = used[1][0] + x
                        cc = used[1][1] 
                        # 종이 안에 있는가
                        if 0 <= cr < N:
                            check(cr, cc, s+paper[cr][cc], cnt+1, used+[(cr,cc)])
            
            check(nr, nc, s+paper[nr][nc], cnt+1, used+[(nr,nc)])


   
max_sum = 0
for r in range(N):
    for c in range(M):
        check(r, c, paper[r][c], 1, [(r,c)])

print(max_sum)