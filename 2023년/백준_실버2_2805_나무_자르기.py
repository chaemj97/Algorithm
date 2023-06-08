'''
    접근법
        자르는 높이 이분탐색
    
'''
import sys
input = sys.stdin.readline

# 나무의 수, 필요한 나무 길이
n,m = map(int,input().split())
tree = list(map(int,input().split()))

answer = 0

l = 0
r = max(tree)
while l <= r:
    mid = (l+r)//2
    
    # mid 높이로 자를 때 나무 길이
    cut = 0
    for i in tree:
        if i > mid:
            cut += (i-mid)
            
    # 나무가 더 필요하다 -> 더 낮은 높이로 잘라야 한다
    if cut < m:
        r = mid - 1
    # 나무가 충분하다 -> 더 높은 높이 가능한지 확인해보자
    else:
        l = mid + 1
        answer = mid

print(answer)