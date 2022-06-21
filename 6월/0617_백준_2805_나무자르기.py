# https://chaemi720.tistory.com/171

from sys import stdin
# 나무의 수 N, 원하는 나무 길이 M
N,M = map(int,stdin.readline().split())
tree = list(map(int,stdin.readline().split()))

# 이진탐색
start,end = 0, max(tree)

while start <= end:
    mid = (start + end)//2

    # 현재 자를 수 있는 나무길이
    log = 0
    for i in tree:
        if i > mid:
            log += i - mid
    
    # 원하는 나무 길이보다 작으면 높이를 down
    # 원하는 나무 길이보다 크면 높이를 up
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)