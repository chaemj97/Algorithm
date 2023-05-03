'''
    접근법 1
        CCW 알고리즘

'''

import sys
input = sys.stdin.readline

# P1, P2, P3
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

# P1P2과 P1P3의 외적 구하기
P1P2 = (x1-x2,y1-y2)
P1P3 = (x1-x3,y1-y3)

# 외적
cross = P1P2[0]*P1P3[1] - P1P2[1]*P1P3[0]

# 일직선?
if cross == 0:
    print(0)
# 반시계?
elif cross > 0:
    print(1)
# 시계?
else:
    print(-1)