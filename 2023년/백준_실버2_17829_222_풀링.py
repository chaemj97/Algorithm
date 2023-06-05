'''
    접근법
        재귀를 통해 구현
    
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def cnn(i,arr):
    # 1x1 
    if i == 1:
        return arr[0][0]

    # 222-풀링
    next = []
    for r in range(0,i,2):
        next_r = []
        for c in range(0,i,2):
            two = [arr[r][c],arr[r][c+1],arr[r+1][c],arr[r+1][c+1]]
            two.sort()
            next_r.append(two[2])
        next.append(next_r)
    return cnn(i//2,next)

print(cnn(n,arr))