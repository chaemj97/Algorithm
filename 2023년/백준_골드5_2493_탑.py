'''
    접근법
        완전 탐색 -> 시간초과
        
        왼쪽 탑들 확인 -> 스택 = [[idx,탑의 높이],...]
            현재 탑보다 높다 -> 수신 가능
            현재 탑보다 낮다 -> 수신 불가능 -> pop    
'''
import sys
input = sys.stdin.readline

# 탑의 수
n = int(input())
# 서로 다른 크기의 탑
top = list(map(int, input().split()))

# 최댓값을 저장
stack = [[0,top[0]]]
answer = [0]*n

for i in range(1,n):
    while stack:
        # 현재 탑보다 크다 -> 수신 가능
        if top[i] < stack[-1][1]:
            answer[i] = stack[-1][0]+1
            break
        # 현재 탑보다 작은 탑 -> 수신 불가능 -> pop
        else:
            stack.pop()
    stack.append([i,top[i]])

print(*answer)