'''
    접근법
        누적합을 통해 최대 방문자 수의 값을 비교 및 갱신
    
'''
from itertools import accumulate
import sys
input = sys.stdin.readline

n,x = map(int,input().split())
# 누적합
visit = [0] + list(accumulate(map(int,input().split())))

answer = 0
cnt = 0
for i in range(n-x+1):
    a = visit[i+x] - visit[i]
    # 최댓값 갱신
    if answer < a:
        answer = a
        cnt = 1
    # 최대 방문자 수 기간 +1
    elif answer == a:
        cnt += 1

# 결과 출력
if answer == 0:
    print('SAD')
else:
    print(answer)
    print(cnt)