'''
    접근법 1
        LIS 알고리즘
'''

import bisect
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

dp = [-float('inf')]
dp_idx = [(-float('inf'),0)]

for i in range(n):
    # 현 증가하는 부분 수열에 추가 가능?
    if dp[-1] < A[i]:
        dp_idx.append((A[i],len(dp)))
        dp.append(A[i])
    # 추가 불가능인 경우
    # 현재 수가 증가하는 부분 수열에 어디 위치에 들어가는지 보고 넣기
    else:
        idx = bisect.bisect_left(dp,A[i])
        dp[idx] = A[i]
        dp_idx.append((A[i],idx))

answer_len = len(dp) - 1
answer = []
# 가장 긴 증가하는 부분 수열 만들기
for num,idx in dp_idx[::-1]:
    if idx == answer_len:
        answer.append(num)
        answer_len -= 1
        if answer_len == 0:
            break
print(len(answer))
print(*answer[::-1])
