# https://chaemi720.tistory.com/184
 
from sys import stdin
input = stdin.readline

# 집의 개수, 공유기의 개수
N, C = map(int,input().split())

# 집의 좌표
house = [int(input()) for _ in range(N)]
house.sort()

# 가장 인접한 두 공유기 사이의 거리를 가능한 크게
# 공유기 사이 최소거리, 최대거리
start = 1
end = house[-1]-house[0]

answer = 0
while start <= end:
    mid = (start+end)//2
    # 공유기 사이 거리를 최소 mid로 할 때 설치할 수 있는 공유기 개수 구하기
    # 시작점 house[0]
    current = house[0]
    cnt = 1
    for i in range(1,len(house)):
        # 다음 공유기까지 거리가 mid 이상?
        if house[i] >= current + mid:
            current = house[i]
            cnt += 1

    # 가장 인접한 두 공유기 사이의 최대 거리
    # 설치하고 싶은 공유기보다 더 적게 설치했으면 -> 거리를 좁히기
    if cnt < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)