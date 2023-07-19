'''
    접근법
        현재 삼각형의 3변의 길이 중 2변 선택해서 평행사변형 만들기
    
'''
import sys
input = sys.stdin.readline

x1,y1,x2,y2,x3,y3 = map(int,input().split())

# 평행사변형을 만들 수 없는 경우
# if (x2-x1)/(y2-y1) == (x3-x1)/(y3-y1):
if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
    print(-1.0)
    sys.exit() 

# 변의 길이
s1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
s2 = ((x1-x3)**2 + (y1-y3)**2)**0.5
s3 = ((x3-x2)**2 + (y3-y2)**2)**0.5

# print(s1,s2,s3)

# 평행사변형의 길이 
answer1 = (s1+s2)*2
answer2 = (s1+s3)*2
answer3 = (s2+s3)*2

print(max(answer1, answer2, answer3) - min(answer1, answer2, answer3))