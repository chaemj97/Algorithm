'''
    접근법 1

'''

import sys
input = sys.stdin.readline

# 친구 수, 성냥 수
n, k = map(int,input().split())
# 친구 방문 시간
time = [int(input()) for _ in range(n)]

# 친구 방문 간격
interval = []
for i in range(1,n):
    interval.append(time[i]-time[i-1])
interval.sort()

answer = n
# n명을 k개의 그룹으로 나누기
for i in range(n-k):
    answer += interval[i]-1
print(answer)