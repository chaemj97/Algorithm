'''
    접근법 1
        4등분시 
            1사분면 2사분면
            3사분면 4사분면
        으로 생각

        2사분면에 있으면 answer이 (2**(N-1))**2은 넘는다.
        3사분면에 있으면 answer이 ((2**(N-1))**2)*2은 넘는다.
        3사분면에 있으면 answer이 ((2**(N-1))**2)*3은 넘는다.
'''

import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())

answer = 0

while N > 0:
    # 4등분
    N -= 1

    # 1사분면에 속하는가?
    if  r < 2**N and c < 2**N:
        answer += 0
    # 2사분면에 속하는가?
    elif r < 2**N and c >= 2**N:
        c -= (2**N)
        answer += (2**N)**2
    # 3사분면에 속하는가?
    elif r >= 2**N and c < 2**N:
        r -= (2**N)
        answer += ((2**N)**2)*2
    # 4사분면에 속하는가?
    else:
        r -= (2**N)
        c -= (2**N)
        answer += ((2**N)**2)*3

print(answer)