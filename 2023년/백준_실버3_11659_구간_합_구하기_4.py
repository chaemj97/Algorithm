'''
    접근법 1
        a번째 수부터 b번째 수까지 합
        -> 구간 합으로 구하기
        num[a-1:b] = num[:b] - num[:a-1]

'''
from itertools import accumulate
import sys
input = sys.stdin.readline

# 수의 개수, 합을 구해야 하는 횟수
N, M = map(int,input().split())
# 수
num = [0] + list(accumulate(map(int,input().split())))

# 구간합
for _ in range(M):
    a,b = map(int,input().split())
    print(num[b]-num[a-1])
