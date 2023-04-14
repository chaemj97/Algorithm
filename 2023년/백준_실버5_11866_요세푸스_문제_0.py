'''
    접근법 1
        que를 활용하여 k번째 사람 구하기
        ex) 5명일때 8번째 사람 구하기 
            -> i : 직전에 제거한 사람 인덱스
               (i+K-1)%len(que)
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
