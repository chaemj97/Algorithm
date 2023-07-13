'''
    접근법
        bfs로 이동
    
'''
from collections import deque
import sys
input = sys.stdin.readline

def game(n):
    # 미로 정보 
    miro = [[0]]
    for _ in range(n):
        room = input().split()
        miro.append([room[0],int(room[1]),list(map(int,room[2:-1]))])
        
    # 방문 표시
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    que = deque()
    # (위치, 가진 돈)
    que.append((1,0))
    while que:
        cur,money = que.popleft()
        
        # 도착?
        if cur == n:
            if miro[cur][0] == 'T':
                if money >= miro[cur][1]:
                    return True
            return True
        
        # 이동
        for d in miro[cur][2]:
            # 자기방에서 자기방으로 이동
            if cur == d:
                continue
            # 다른방으로 이동
            # 1. 트롤인 경우
            if miro[d][0] == 'T':
                if visited[d] == 0:
                    # 통행료를 내야 들어갈 수 있다.
                    if money >= miro[d][1]:
                        visited[d] = 1
                        que.append((d,money-miro[d][1]))
                        
            # 2. 레프리콘인 경우
            elif miro[d][0] == 'L':
                if visited[d] == 0:
                    # 일정량 미만이면 채우기
                    # 일정량 이상이면 그대로
                    money = max(money,miro[d][1])
                    visited[d] = 1
                    que.append((d,money))
            
            # 3. 빈 방인 경우
            else:
                if visited[d] == 0:
                    visited[d] = 1
                    que.append((d,money))
                    
    # n번 방 도착 못함
    return False


while True:
    n = int(input())
    # 미로 끝
    if n == 0:
        break
    
    if game(n):
        print('Yes')
    else:
        print('No')