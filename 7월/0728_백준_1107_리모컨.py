

from sys import stdin
input = stdin.readline

# 이동하려고 하는 채널
N = int(input())
# 고장난 버튼 개수
M = int(input())
# 고장난 숫자 버튼
broken = list(map(int,input().split()))

# 1. 100번에서 +,-로만 움직이는 경우(ex) 101,99...)
min_cnt = abs(100-N)

# 2. 숫자 버튼도 사용한 경우
# 이동하려고 하는 채널 최대 500,000이니 최대 누를 수 있는 채널 1,000,000
for num in range(1000001):
    num = str(num)
    for n in range(len(num)): 
        # 누를 수 없는 버튼이 있다면 pass
        if int(num[n]) in broken:
            break
        # 다 누를 수 있을 때(마지막 숫자 버튼 누를 때)
        elif n == len(num)-1:
            min_cnt = min(min_cnt, abs(N-int(num)) + len(num))

print(min_cnt)
