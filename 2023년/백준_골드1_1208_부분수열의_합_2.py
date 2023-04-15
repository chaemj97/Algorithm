'''
    접근법 1
        N은 최대 40 -> 부분 수열의 개수 2**40 -> 너무 크다
        수열을 반으로 나누기
        (2**20)*2 = 2**21 -> 연산량이 훨씬 줄어든다

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
    for i in range(1,l+1):
        for cnt in combinations(arr,i):
            s = sum(cnt)
            result.append(s)
    return sorted(result)

A_sum = sub_sum(A)
B_sum = sub_sum(B)
# S가 있는 경우
answer = A_sum.count(S) + B_sum.count(S)

for i in range(len(A_sum)):
    left = bisect.bisect_left(B_sum,S-A_sum[i])
    right = bisect.bisect_right(B_sum,S-A_sum[i])
    answer += right - left
print(answer)