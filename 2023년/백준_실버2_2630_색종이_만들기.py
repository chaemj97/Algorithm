'''
    접근법 1
        같은 색이 존재하지 않는다면 재귀를 사용하여 나누기
'''

import sys
input = sys.stdin.readline

N = int(input()) # 2, 4, 8, 16, 32, 64, 128 중 하나
arr = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0
def check(s_r,s_c,l):
    global white, blue

    # 하나의 정사각형 칸
    if l == 0:
        if arr[s_r][s_c] == 1:
            blue += 1
        else:
            white += 1

    color = arr[s_r][s_c]
    for r in range(s_r,s_r+l):
        for c in range(s_c,s_c+l):
            # 다른 색이 섞여 있다 -> 자르자
            if arr[r][c] != color:
                check(s_r,s_c,l//2)
                check(s_r,s_c+l//2,l//2)
                check(s_r+l//2,s_c,l//2)
                check(s_r+l//2,s_c+l//2,l//2)
                return

    # 색종이에 같은 색만 존재한다.
    if color == 1:
        blue += 1
    else:
        white += 1

check(0,0,N)
print(white)
print(blue)
