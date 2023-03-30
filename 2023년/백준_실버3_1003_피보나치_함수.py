'''
    접근법 1
        0이 나오는 횟수 : 1,0,1,1,2,3,...
        1이 나오는 횟수 : 0,1,1,2,3,...

        0이 나오는 횟수는 첫번째를 제외하면 n-1일 때 1이 나오는 횟수

'''

import sys
input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())

for tc in range(T):
    n = int(input())
    # 0이 나올 횟수, 1이 나올 횟수
    zero,one = 1,0
    for i in range(n):
        zero,one = one,zero+one
    
    print(zero,one)