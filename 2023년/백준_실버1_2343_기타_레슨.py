'''
    접근법
        블루레이 크기 기준으로 이분 탐색
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

# 이분 탐색 기준 : 블루레이 크기
l = min(arr)
r = sum(arr)

answer = sum(arr)
while l <= r:
    mid = (l+r)//2
    # 블루 레이 최대 크기는 max(arr)보다 커야 함
    if mid < max(arr):
        l = mid + 1
        continue
    
    # 블루레이 최대 크기가 mid일때 블루레이 개수
    cnt = 1
    s = 0
    for i in range(n):
        if s + arr[i] <= mid:
            s += arr[i]
        else:
            cnt += 1
            s = arr[i]

    # 블루레이 개수가 적거나 같다 -> 늘리자
    if cnt <= m:
        r = mid - 1
        answer = min(answer,mid)
    else:
        l = mid + 1 
        
print(answer)