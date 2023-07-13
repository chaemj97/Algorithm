'''
    접근법
        과자의 길이 이분탐색으로 찾기
    
'''
import sys
input = sys.stdin.readline

# 조카 수, 과자 수
n,m = map(int,input().split())
snack = list(map(int,input().split()))

answer = 0
l = 1
r = max(snack)
while l <= r:
    # 막대 과자 길이
    mid = (l+r)//2
    # 나눠 줄 수 있는 조카 수
    cnt = 0
    for i in snack:
        cnt += i//mid
        
    # 모든 조카에게 나눠줄 수 있다.
    # -> 더 긴 막대 과자를 줄 수 있는지 확인해보자
    if cnt >= n:
        l = mid + 1 
        answer = mid
    # 모든 조카에게 나눠줄 수 없다.
    # -> 막대 과자의 길이를 줄이자
    else:
        r = mid - 1
        
# 결과 출력
print(answer)