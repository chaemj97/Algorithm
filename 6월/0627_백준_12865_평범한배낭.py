

from sys import stdin
input = stdin.readline

# 물품의 수, 준서가 버틸수 있는 무게
N, K = map(int, input().split())
# [[물건의 무게, 해당 물건의 가치],...]
things = []
for _ in range(N):
    # 물건의 무게, 해당 물건의 가치
    w,v = map(int, input().split())
    # 물건의 무게 당 가치
    s = w/v
    # [무게당 가치, 무게, 가치]
    things.append([s,w,v])

# 정렬 (무게 당 가치가 높은 순, 무게가 가벼운 순)
things.sort(key = lambda x: (-x[0],x[1]))

# 물건들의 가치합의 최대값을 구하라
# 배낭에 넣을 수 있는 만큼 넣기
i = 0
max_value = 0
while K > 0 and i < N:
    if K - things[i][1] >= 0:
        K -= things[i][1]
        max_value += things[i][2]
    i += 1


print(max_value)