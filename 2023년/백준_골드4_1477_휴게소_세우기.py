'''
    접근법
        휴게소 간의 간격 이분 탐색
            추가 설치한 휴게소의 수가 m보다 많으면 간격 늘리기
            
'''

import sys
input = sys.stdin.readline

# 현재 휴게소의 수, 추가 휴게소의 수, 고속도로 길이
N,M,L = map(int,input().split())
now = [0] + list(map(int,input().split())) + [L]
now.sort()

l = 1
r = L-1
answer = 0
while l <= r:
    mid = (l+r)//2
    # 이번 간격(mid)에서 추가 설치할 수 있는 휴게소 수
    cnt = 0
    for i in range(1,N+2):
        interval = now[i]-now[i-1]
        # 간격이 mid보다 크다? -> 그 사이 사이에 휴게소 설치
        if interval > mid:
            cnt += (interval-1)//mid

    # 휴게소를 더 설치해야하는가? -> 간격을 더 작게
    if cnt <= M:
        r = mid-1
        answer = mid
    # 휴게소가 너무 많은가? -> 간격을 더 크게
    else:
        l = mid + 1

print(answer)