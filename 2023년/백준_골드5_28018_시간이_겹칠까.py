'''
    접근법
        각 시간에 몇명이 있는지 구해야 함
        학생이 앉은 시간 다 입력하면 시간초과
        -> 누적합 사용하기
        
        예제 2
        time = [0, 0, 0, 0, 0, 0, 0, 0]
        1 5
        3 6
        목표 = [0, 1, 1, 2, 2, 2, 1, 0]
        
        누적합
        시작 시간 += 1
        끝나는 시간+1 -= 1
        time = [0, 1, 0, 1, 0, 0, -1, -1]
        list(accumulate(time)) = [0, 1, 1, 2, 2, 2, 1, 0]
    
'''
from itertools import accumulate
import sys
input = sys.stdin.readline

# 학생 수
n = int(input())
time = [0 for _ in range(10**6+2)]
for _ in range(n):
    s,e = map(int,input().split())
    time[s] += 1
    time[e+1] -= 1 

# 누적합
acc_time = list(accumulate(time))

# 특정한 시각의 개수
q = int(input())
spe = list(map(int,input().split()))
for i in spe:
    print(acc_time[i])