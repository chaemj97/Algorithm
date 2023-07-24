'''
    접근법
        파닭에 넣을 파의 길이 이분탐색
    
'''
import sys
input = sys.stdin.readline

# 파의 개수, 파닭의 개수
s,c = map(int,input().split())
# 파의 길이
lenght = list(int(input()) for _ in range(s))
lenght.sort()

l = 1
r = lenght[-1]
answer = 0 

while l <= r:
    # 파닭에 넣을 파의 길이
    mid = (l+r)//2
    # 가능한 파의 개수
    cnt = 0
    
    for i in lenght:
        cnt += (i//mid)
        
    # 파의 개수가 충분하다?
    # 파의 길이를 늘려보자
    if cnt >= c:
        l = mid + 1
        # 라면에 넣을 파의 길이
        answer = sum(lenght) - mid*c
    # 파의 길이가 부족하다
    # 파의 길이를 줄여보자
    else:
        r = mid - 1

print(answer)