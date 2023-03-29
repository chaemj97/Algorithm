'''
    접근법 1
        한바퀴가 끝나는 지점
        1, 7, 19, 37, 61 ... 
        차이
        6, 12, 18, 24
        -> An = 1 + (6 + 12 + ... + 6*(n-1))
              = 1 + 6((n-1)*n/2)
              = 3*n^2 - 3*n + 1

        ex) N = 13
            A2 < 13 <= A3
            -> 답은 3
'''

import sys
input = sys.stdin.readline

N = int(input())

def func(n):
    # an = 1 + (6 + 12 + ... + 6*(n-1))
    return 3*n**2-3*n+1

n = 1
while True:
    if N <= func(n):
        print(n)
        break
    else:
        n += 1