'''
    접근법 1
        최대한 많은 회의를 하고 싶다.
            -> 회의 시간이 짧을수록 좋다?
            -> 빨리 끝나고 일찍 시작       
            -> 다음 회의의 시작시간은 이전 회의의 종료시간 이후여야 함

'''

import sys
input = sys.stdin.readline

# 회의의 수
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

# 최대한 많은 회의를 하고 싶다.
# 빨리 끝나고 일찍 시작하는 순서
arr.sort(key=lambda x: (x[1],x[0]))
answer = 1
end_time = arr[0][1]
for i in range(1,N):
    # 다음 회의의 시작시간은 이전 회의의 종료시간 이후여야 함
    if arr[i][0] >= end_time:
        answer += 1
        end_time = arr[i][1]
        
print(answer)