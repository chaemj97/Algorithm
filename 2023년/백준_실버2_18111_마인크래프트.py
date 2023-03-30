'''
    접근법 1
        땅의 최저 높이 ~ 땅의 최고 높이까지 완전 탐색

        i 높이에서 땅을 고르는데 걸리는 시간을 구하기
        그 시간이 최저면 갱신

'''

import sys
input = sys.stdin.readline

# 세로, 가로, 인벤토리에 블록 수
N,M,B = map(int,input().split())

# 땅의 높이
height = []

min_height,max_height = float('inf'),0
for _ in range(N):
    h = list(map(int,input().split()))
    height.append(h)
    min_height = min(min_height,*h)
    max_height = max(max_height,*h)
             
answer_time,answer_height = float('inf'),0

# 땅의 높이는 0~256
# i : 목표 땅의 높이
for i in range(min_height,max_height+1):
    # 추가한 블록, 철거한 블록
    add_block, take_block = 0,0

    for r in range(N):
        for c in range(M):
            # 목표 땅보다 높으면 철거 
            if height[r][c] > i:
                take_block += (height[r][c] - i)
            # 목표 땅보다 낮으면 추가
            else:
                add_block += (i - height[r][c])
    
    # 추가한 블록은 (철거한 블록 + 인벤토리에 저장한 블록)보다 작아야 함
    if add_block > take_block + B:
        continue

    # 시간
    time = add_block + take_block * 2

    # 최소 시간인가?
    if answer_time >= time:
        answer_time = time
        answer_height = i
    
print(answer_time,answer_height)
