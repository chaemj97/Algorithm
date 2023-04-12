'''
    접근법 1
        () 의 의미 : 4등분 한 것을 묶을 때 사용
        4등분 -> 분할정복

'''

import sys
input = sys.stdin.readline

# 영상의 크기
N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

# (r,c) : 현 구간의 가장 왼쪽 위
# l : 구간의 가로(세로) 길이
def sol(r,c,l):
    # 이 구간에 수가 한개라면?
    if l == 1:
        return arr[r][c]
    
    start = arr[r][c]
    for i in range(l):
        for j in range(l):
            # 구간 내에 다른 숫자가 있다?
            if arr[r+i][c+j] != start:
                # 4등분 하자
                a = '('
                a += sol(r,c,l//2)
                a += sol(r,c+l//2,l//2)
                a += sol(r+l//2,c,l//2)
                a += sol(r+l//2,c+l//2,l//2)
                a += ')'
                return a
    # 이 구간의 모든 숫자가 같다
    return start
    
print(sol(0,0,N))
