'''
    접근법
        n개의 원판이 있을 때
        1. 맨 밑의 원판을 제외하고 나머지 n-1개의 원판을 1번에서 2번으로 옮기기
        2. 맨 밑의 원판을 1번에서 3번으로 옮기기
        3. 2번에 있는 n-1개의 원판을 3번으로 옮기기
    
'''

import sys
input = sys.stdin.readline

n = int(input())

# num : 옮겨야 하는 탑 수
def hanoi(num,a,b,c):
    # 다 옮겼는가?
    if num == 0:
        return
    # 1번
    hanoi(num-1,a,c,b)
    # 2번
    print(a,c)
    # 3번
    hanoi(num-1,b,a,c)
    
print(2**n-1)
hanoi(n,1,2,3)