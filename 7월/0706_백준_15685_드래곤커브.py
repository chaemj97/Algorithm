

from sys import stdin
input = stdin.readline

# 격자 크기 100*100(0<=r<=100, 0<=c<=100)
# 격자 꼭짓점
arr = [[0]*101 for _ in range(101)]

# 드래곤 커브의 개수
N = int(input())
# 방향
# 가로 세로 체크!!
# 가로(x) c, 세로(y) r
direction = [[0,1],[-1,0],[0,-1],[1,0]]

# 드래곤 커브
for _ in range(N):
    # 드래곤 커브의 정보
    # 시작점(x,y), 시작 방향(d), 세대(g)
    y,x,d,g = map(int,input().split())
    arr[x][y] = 1
    # 이동방향 나열
    moves = [d]
    # 1~g세대
    for K in range(1,g+1):
        # 다음 세대 드래곤 커브
        for i in range(len(moves)-1,-1,-1):
            moves.append((moves[i]+1)%4)

    # g세대 드래곤 커브 표시
    for move in moves:
        x += direction[move][0]
        y += direction[move][1]
        arr[x][y] = 1
        
# 90도 시계 방향 회전
# 0 -> 1
# 1 -> 2
# 2 -> 3
# 3 -> 0
# 결과 i -> (i+1) % 4

# 세대
# 0 : 0
# 1 : 0 1
# 2 : 01 21
# 3 : 0121 2321
# 4 : 01212321 23032321


# 결과
# 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수
result = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] == arr[r][c+1] == arr[r+1][c] == arr[r+1][c+1] == 1:
            result += 1
print(result)