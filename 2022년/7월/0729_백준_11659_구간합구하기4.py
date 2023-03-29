from sys import stdin
input = stdin.readline

# 수의 개수, 합을 구해야 하는 횟수
N, M = map(int,input().split())
# 수
num = list(map(int,input().split()))

for _ in range(M):
    i, j = map(int,input().split())
    print(sum(num[i-1:j]))

