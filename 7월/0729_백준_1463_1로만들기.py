

from sys import stdin
input = stdin.readline

N = int(input())
cnt = [100000]*(N+1)
cnt[N] = 1
for i in range(N,0,-1):
    # 3으로 나누어 떨어짐
    if i % 3 == 0:
        cnt[i//3] = min(cnt[i//3],cnt[i]+1)
    # 2로 나누어 떨어짐
    if i % 2 == 0:
        cnt[i//2] = min(cnt[i//2],cnt[i]+1)
    # 1빼기
    cnt[i-1] = min(cnt[i-1],cnt[i]+1)
print(cnt[1]-1)

