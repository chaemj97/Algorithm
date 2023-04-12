'''
    접근법 1
        bfs를 활용하여 연결된 동그라미 색 확인
            색칠한 적 없는 동그라미 
                현재 색이랑 반대 색 등록
            색칠한 적 있는 동그라미
                현재 색이랑 같으면 -> impossible
                다르면 pass
                
        전체가 연결이 되어 있지 않다!!
'''
from collections import deque
import sys
input = sys.stdin.readline

def sol(i):
    global answer
    # i번부터 색 결정하자
    que = deque()
    que.append(i)
    checked[i] = 0
    
    while que:
        # 현 위치
        c = que.popleft()
        # c와 연결된 동그라미 확인
        for d in edge[c]:
            # 색칠한 적 없는 동그라미
            if checked[d] == -1:
                checked[d] = (checked[c]+1)%2
                que.append(d)
            # 색칠한 동그라미인데 c랑 색이 같아 -> 실패
            elif checked[d] == checked[c]:
                answer = 'impossible'
                return 

TC = int(input())
for _ in range(TC):
    # 동그라미의 개수, 직선들의 개수
    n,m = map(int,input().split())
    
    # 연결리스트
    edge = [[] for _ in range(n)]
    for _ in range(m):
        x,y = map(int,input().split())
        edge[x-1].append(y-1)
        edge[y-1].append(x-1)
    
    # 색칠 여부
    checked = [-1]*(n)
    
    # 기본값
    answer = 'possible'
    
    for i in range(n):
        # 아직 확인되지 않은 동그라미가 남아있다면
        if checked[i] == -1:
            sol(i)
            if answer == 'impossible':
                break
    print(answer)