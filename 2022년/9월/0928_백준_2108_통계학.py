from collections import Counter
import sys
input = sys.stdin.readline
# 수의 개수
N = int(input())
number = [int(input()) for _ in range(N)]
number.sort()
# 산술평균
print(round(sum(number)/N))
# 중앙값
print(number[(N-1)//2])
# 최빈값
cnt = Counter(number).most_common()
# 최빈값 2개이상인가?
if len(cnt) >= 2:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0]) 
# 범위
print(max(number)-min(number))