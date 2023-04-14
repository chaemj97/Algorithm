'''
    접근법 1

'''
import bisect
from itertools import combinations
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))
 
A = arr[:N//2]
B = arr[N//2:]
# 부분 수열의 합
def sub_sum(arr):
    result = []
    l = len(arr)
    for i in range(l):
        s = 0
        for j in range(i,l):
            s += arr[j]
            result.append(s)
    return sorted(result)

A_sum = sub_sum(A)
B_sum = sub_sum(B)
answer = 0
for i in range(len(A_sum)):
    left = bisect.bisect_left(B_sum,S-A_sum[i])
    right = bisect.bisect_right(B_sum,S-A_sum[i])
    answer += right - left
print(answer)