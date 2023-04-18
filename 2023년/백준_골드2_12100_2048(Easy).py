'''
    접근법 1
        최대 5번 상하좌우 밀기 4**5 -> 완전 탐색
'''
from copy import deepcopy
import sys
input = sys.stdin.readline

# 보드의 크기
N = int(input())
game = [list(map(int,input().split())) for _ in range(N)]

def move(game,d):
    # 왼쪽으로 밀기
    if d == 0:
        for r in range(N):
            cursor = 0
            for c in range(1,N):
                # 숫자가 있다.
                if game[r][c]:
                    tmp,game[r][c] = game[r][c],0
                    # 밀기
                    if game[r][cursor] == 0:
                        game[r][cursor] = tmp
                    # 합치기
                    elif game[r][cursor] == tmp:
                        game[r][cursor] = tmp*2
                        cursor += 1
                    # 합칠 순 없고 밀기    
                    else:
                        cursor += 1
                        game[r][cursor] = tmp                
    # 오른쪽으로 밀기
    elif d == 1:
        for r in range(N):
            cursor = N-1
            for c in range(N-2,-1,-1):
                if game[r][c]:
                    tmp, game[r][c] = game[r][c], 0
                    if game[r][cursor] == 0:
                        game[r][cursor] = tmp
                    elif game[r][cursor] == tmp:
                        game[r][cursor] = tmp*2
                        cursor -= 1
                    else:
                        cursor -= 1
                        game[r][cursor] = tmp
    # 위쪽으로 밀기
    elif d == 2:
        for c in range(N):
            cursor = 0
            for r in range(1,N):
                if game[r][c]:
                    tmp,game[r][c] = game[r][c],0
                    if game[cursor][c] == 0:
                        game[cursor][c] = tmp
                    elif game[cursor][c] == tmp:
                        game[cursor][c] = tmp*2
                        cursor += 1
                    else:
                        cursor += 1
                        game[cursor][c] = tmp
    # 아래쪽으로 밀기
    else:
        for c in range(N):
            cursor = N-1
            for r in range(N-2,-1,-1):
                if game[r][c]:
                    tmp, game[r][c] = game[r][c], 0
                    if game[cursor][c] == 0:
                        game[cursor][c] = tmp
                    elif game[cursor][c] == tmp:
                        game[cursor][c] = tmp*2
                        cursor -= 1
                    else:
                        cursor -= 1
                        game[cursor][c] = tmp
    return game

# 게임 횟수
def dfs(game,cnt):
    global answer
    # 5번 이동했는가?
    if cnt == 5:
        # 가장 큰 블록 갱신
        for i in range(N):
            answer = max(*game[i],answer)
        return
    
    # 4방향 이동
    for d in range(4):
        next_game = move(deepcopy(game),d)
        dfs(next_game, cnt+1)
    
answer = 0
dfs(game,0)

print(answer)