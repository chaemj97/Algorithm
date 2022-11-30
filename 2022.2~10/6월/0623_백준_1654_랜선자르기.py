# https://chaemi720.tistory.com/182

from sys import stdin

input = stdin.readline

# 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
K,N = map(int,input().split())

# 가지고 있는 랜선 길이
lines = []
for _ in range(K):
    l = int(input())
    lines.append(l)

# 이분 탐색
start = 1
end = max(lines) 

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    # 랜선 자르기
    for line in lines:
        cnt += line // mid
    # 잘린 랜선이 원하는 갯수보다 많다면 길이를 늘리기
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
