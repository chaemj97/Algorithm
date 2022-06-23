

from sys import stdin
input = stdin.readline

# 집의 개수, 공유기의 갯
N, C = map(int,input().split())

# 집의 좌표
house = []
for i in range(N):
    h = int(input())
    house.append(h)

house.sort()

# 집끼리 거리
dist = []
