'''
    접근법 1
        재귀를 활용

'''

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

zero = 0
one = 0
minus = 0

def check(s_r,s_c,l):
    global zero,one,minus

    # 하나의 정사각형 칸
    if l == 0:
        if arr[s_r][s_c] == 0:
            zero += 1
        elif arr[s_r][s_c] == 1:
            one += 1
        else:
            minus += 1

    num = arr[s_r][s_c]
    for r in range(s_r,s_r+l):
        for c in range(s_c,s_c+l):
            # 다른 수가 섞여 있다 -> 자르자
            if arr[r][c] != num:
                check(s_r,s_c,l//3)
                check(s_r,s_c+l//3,l//3)
                check(s_r,s_c+l//3*2,l//3)
                check(s_r+l//3,s_c,l//3)
                check(s_r+l//3,s_c+l//3,l//3)
                check(s_r+l//3,s_c+l//3*2,l//3)
                check(s_r+l//3*2,s_c,l//3)
                check(s_r+l//3*2,s_c+l//3,l//3)
                check(s_r+l//3*2,s_c+l//3*2,l//3)
                return

    # 종이에 같은 수로만 존재한다.
    if num == 0:
        zero += 1
    elif num == 1:
        one += 1
    else:
        minus += 1


check(0,0,N)
print(minus)
print(zero)
print(one)
