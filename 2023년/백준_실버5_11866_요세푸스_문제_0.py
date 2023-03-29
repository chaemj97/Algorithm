'''
    접근법 1

'''

import sys
input = sys.stdin.readline

# N명의 사람, K번째 제거
N,K = map(int,input().split())

que = [i for i in range(1,N+1)]
print('<',end='')
i = 0
while que:
    i = (i+K-1)%len(que)
    if len(que) == 1:
        print(f'{que.pop(i)}>')
    else:
        print(f'{que.pop(i)}, ',end='')
