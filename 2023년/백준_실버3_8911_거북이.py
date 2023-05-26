'''
    접근법
        이동한 위치의 가로 세로 구하기
        구현
    
'''

import sys
input = sys.stdin.readline

# 오른쪽 방향
d = [[-1,0],[0,1],[1,0],[0,-1]]
T = int(input())
for _ in range(T):
    control = list(input().rstrip())
    
    # 현재 방향
    direction = 0
    # 현재 위치
    current_r,current_c = 0,0
    # 방문한 곳
    visited_r = [0]
    visited_c = [0]
    for c in control:
        # 앞으로 한 칸
        if c == 'F':
            current_r += d[direction][0]
            current_c += d[direction][1]
            visited_r.append(current_r)
            visited_c.append(current_c)
        
        # 뒤로 한 칸
        elif c == 'B':
            current_r -= d[direction][0]
            current_c -= d[direction][1]
            visited_r.append(current_r)
            visited_c.append(current_c)
        
        # 오른쪽으로 90도 회전
        elif c == 'R':
            direction = (direction + 1)%4
            
        # 왼쪽으로 90도 회전
        elif c == 'L':
            direction = (direction - 1)%4
    
    # 이동한 영역을 모두 포함하는 가장 작은 직사각형 넓이 구하기
    h = max(visited_r) - min(visited_r)
    v = max(visited_c) - min(visited_c)
    print(h*v)