'''
    접근법
        1. 일직선 거리 >= d
            1. 걷기
            2. 점프 n번 후 남은 만큼 걷기
            3. 점프 n+1번 후 넘은 만큼 되돌아가기
            4. 점프만으로 도착?
            
        2. 일직선 거리 < d
            1. 걷기
            2. 점프 1번 후 넘은 만큼 되돌아가기
            3. 점프 2번 (이등변 삼각형 d가 2개)
    
'''
import sys
input = sys.stdin.readline

x,y,d,t = map(int,input().split())

# 일직선 거리
dist = (x**2+y**2)**0.5

# 1. 일직선 거리 >= d
if dist >= d:
    # 1. 걷기
    one = dist
    # 2. 점프 n번 후 남은 만큼 걷기
    jump = dist//d
    two = jump*t + (dist - (jump*d))
    # 3. 점프 n+1번 후 넘은 만큼 되돌아가기
    three = (jump+1)*t + ((jump+1)*d - dist)
    # 4. 점프만으로 도착?
    four = (jump+1)*t
    
    print(min(one,two,three,four))
# 2. 일직선 거리 < d
else:
    # 1. 걷기
    one = dist
    # 2. 점프 1번 후 넘은 만큼 되돌아가기
    two = t + (d-dist)
    # 3. 점프 2번 (이등변 삼각형 d가 2개)
    three = t*2
    
    print(min(one,two,three))