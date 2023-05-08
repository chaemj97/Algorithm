'''
    접근법 
        완전탐색
        모음의 개수 1이상, 자음의 개수 2이상이면 출력
    
'''
from itertools import combinations
import sys
input = sys.stdin.readline

# c개의 문자 중 n개 사용
n,c = map(int,input().split())
arr = list(input().split())
arr.sort()
for c in combinations(arr,n):
    # 모음의 개수
    cnt = 0
    for s in ['a','e','i','o','u']:
        cnt += c.count(s)
    # 모음의 개수 1이상, 자음의 개수 2이상
    if cnt >= 1 and n - cnt >= 2:
        print(''.join(c))
