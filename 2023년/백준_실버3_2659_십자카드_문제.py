'''
    접근법
        완전 탐색
    
'''
import sys
input = sys.stdin.readline

a,b,c,d = input().split()

# 시계수 4가지 중 가장 작은거 구하기
def check(a,b,c,d):
    target = min(a+b+c+d,
                 b+c+d+a,
                 c+d+a+b,
                 d+a+b+c)
    return target

target = check(a,b,c,d)

answer = 0
for i in range(1111,int(target)+1):
    i = str(i)
    if '0' not in i:
        if i == check(i[0],i[1],i[2],i[3]):
            answer += 1

print(answer)
