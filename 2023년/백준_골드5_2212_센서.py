'''
    접근법 1        
        집중국의 수신 가능 역역은 고속도로 상에서 연결된 구간을 나타나게 된다. 
        즉. 특정 위치에 집중국을 설치하는 것이 아닌 "범위"로 수신 가능 영역을 조절하고 수신 가능 영역의 길이의 합을 최소화
        
        -> 센서를 K개의 그룹으로 나눈다!
'''

import sys
input = sys.stdin.readline

# 센서의 개수
N = int(input())
# 집중국의 개수
K = int(input())
# 센서의 좌표
sensor = sorted(map(int,input().split()))

# 집중국 >= 센서
if K >= N:
    print(0)
    sys.exit()
    
# 각 센서의 거리 차이
d = []
for i in range(N-1):
    d.append(sensor[i+1]-sensor[i])
d.sort(reverse=True)

# K개의 영역만 남기기
print(sum(d[K-1:]))            