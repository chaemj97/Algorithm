'''
    접근법 1
        종말의 수
            : 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수

        -> 완전 탐색
'''

import sys
input = sys.stdin.readline

# N번째 영화
N = int(input())

n = 665
while N > 0:
    n  += 1
    if '666' in str(n):
        N -= 1
    
print(n)