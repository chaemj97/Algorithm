'''
    접근법 1
        현재 위치가 이전 위치의 원소들보다 크면 dp에 추가
        작으면, bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 index를 구한다
            그리고 dp의 index 원소를 A[i]로 바꾼다

'''
import bisect
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

# 가장 긴 증가하는 부분 수열을 저장할 배열
dp = [A[0]]

for i in range(N):
    # 현재 위치가 이전 위치의 원소들보다 크면 dp에 추가
    if A[i] > dp[-1]:
        dp.append(A[i])
    # 작으면, bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 index를 구한다
    # 그리고 dp의 index 원소를 A[i]로 바꾼다
    else:
        idx = bisect.bisect_left(dp,A[i])
        dp[idx] = A[i]
print(len(dp))
