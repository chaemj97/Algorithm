'''
    접근법
        x위치, y위치 따로 저장
        구현
'''

import sys
input = sys.stdin.readline

# 네잎 클로버의 개수, 명령 수
n,m = map(int,input().split())
# (-100,000 < Xi, Yi < 100,000) -> (0 < Xi+100,000 < 200,000)
clover_x = [[] for _ in range(200000)]
clover_y = [[] for _ in range(200000)]
for _ in range(n):
    x,y = map(int,input().split())
    clover_x[x+100000].append(y+100000)
    # clover_x[x+100000].sort()
    
    clover_y[y+100000].append(x+100000)
    # clover_y[y+100000].sort()

for i in range(200000):
    if clover_x[i]:
        clover_x[i].sort()
    if clover_y[i]:
        clover_y[i].sort()

order = list(input().rstrip())

# 현 위치 (0,0) -> (100000,100000)
current_x,current_y = 100000,100000

for i in order:
    # 왼쪽 이동
    if i == 'L':
        # x의 좌표가 현재보다 낮은게 나오면 그 값
        for i in clover_y[current_y][::-1]:
            if i < current_x:
                current_x = i
                break
    
    # 오른쪽 이동 
    elif i == 'R':
        # x의 좌표가 현재보다 큰게 나오면 그 값
        for i in clover_y[current_y]:
            if i > current_x:
                current_x = i
                break
        
    # 위로 이동
    elif i == 'U':
        # y의 좌표가 현재보다 큰게 나오면 그 값
        for i in clover_x[current_x]:
            if i > current_y:
                current_y = i
                break
    
    # 아래로 이동
    elif i == 'D':
        # y의 좌표가 현재보다 큰게 나오면 그 값
        for i in clover_x[current_x][::-1]:
            if i < current_y:
                current_y = i
                break
    
print(current_x-100000,current_y-100000)
    
