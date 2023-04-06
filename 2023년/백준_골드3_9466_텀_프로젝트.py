'''
    접근법 1
        dfs를 활용하여 cycle이 있는지 확인!
        있다면 팀으로 묶기
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 학생 사이클 확인
def dfs(x):

    global result
    used[x] = 1
    cycle.append(x)
    number = num[x] # x가 선택한 학생

    if used[number]:
        # 사이클 가능?
        if number in cycle:
            # 이번 팀에 속한 학생들
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    # 학생 수
    n = int(input())
    # 선택된 학생 번호
    num = [0]+list(map(int,input().split()))

    # 확인된 학생
    used = [1]+[0]*n

    # 팀에 속한 학생들
    result = []

    for i in range(1,n+1):
        # 확인한 적 없는 학생
        if used[i] == 0:
            cycle = []
            dfs(i)

    print(n - len(result))