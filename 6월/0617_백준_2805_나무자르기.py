from sys import stdin
# 나무의 수 N, 원하는 나무 길이 M
N,M = map(int,stdin.readline().split())
tree = list(map(int,stdin.readline().split()))

# 절단기에 설정할 수 있는 최대 높이
height = max(tree)
cnt = 0
while M > 0 and height > 0:
    cnt += tree.count(height)
    M -= cnt
    height -= 1

print(height)
