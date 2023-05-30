'''
    접근법
        n이 최대 8이기 때문에 모든 경우 8! == 40320
        -> 완전 탐색 가능
    
'''
from itertools import permutations
import sys
input = sys.stdin.readline


# n 최대 8
n,k = map(int,input().split())
arr = list(map(int,input().split()))

answer = 0
# 모든 경우
for p in permutations(arr,n):
    muscle = 500
    for i in p:
        muscle = muscle + i -k
        # 근손실이 났는가?
        if muscle < 500:
            break
    # 근손실이 나지 않았다.
    else:
        answer += 1
print(answer)