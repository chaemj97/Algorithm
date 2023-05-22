'''
    접근법
        ccw 알고리즘
    
'''

import sys
input = sys.stdin.readline

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

def ccw(a1,b1,a2,b2,a3,b3):
    # P1, P2, P3 -> P1P2에서 P3
    # P2P1과 P3P1의 CCW
    return (a2-a1)*(b3-b1) - (b2-b1)*(a2-a1)

ccw123 = ccw(x1,y1,x2,y2,x3,y3)
ccw124 = ccw(x1,y1,x2,y2,x4,y4)
ccw341 = ccw(x3,y3,x4,y4,x1,y1)
ccw342 = ccw(x3,y3,x4,y4,x2,y2)

if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
    # 평행 + 겹쳐짐
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
        print(1)
    else:
        print(0)

else:
    # 교차
    if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
        print(1)
    else:
        print(0)