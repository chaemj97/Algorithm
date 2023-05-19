'''
    접근법
    
'''

import sys
input = sys.stdin.readline

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

def ccw(a1,b1,a2,b2,a3,b3):
    # P1, P2, P3 -> P1P2에서 P3
    # P2P1과 P3P1의 CCW
    return (a2-a1)*(b3-b1) - (b2-b1)*(a2-a1)

ccw123 = ccw(x1,y1,x2,y2,x3,y3)
ccw124 = ccw(x1,y1,x2,y2,x4,y4)
ccw341 = ccw(x3,y3,x4,y4,x1,y1)
ccw342 = ccw(x3,y3,x4,y4,x2,y2)

# 평행
if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
    pass
# '여기다'
else:
    # 교차
    if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
        print(1)
    else:
        print(0)