'''
    접근법 1
        재료의 개수 최대 10개
        각 재료를 넣고 빼고 2**10 == 1024
        모든 경우 탐색
'''

import sys
input = sys.stdin.readline

# 재료의 개수 <= 10
N = int(input())
food = [list(map(int,input().split())) for _ in range(N)]

answer = float('inf')
# i : 음식 번호, a : 신맛, b : 쓴맛, cnt : 사용한 음식 수
def cook(i,a,b,cnt):
    global answer
    # 다 확인했는가?
    if i == N:
        # 음식을 1개 이상 사용했고 신맛과 쓴맛의 차이 최소인가?
        if cnt != 0 and abs(a-b) < answer:
            answer = abs(a-b)
        return
    
    # 다음 음식 추가
    cook(i+1,a*food[i][0],b+food[i][1],cnt+1)
    # 다음 음식 추가X
    cook(i+1,a,b,cnt)
    
cook(0,1,0,0)
print(answer)