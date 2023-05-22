'''
    접근법
        combinations([i for i in range(n)],n//2)
        ex) n == 3 (20개)
        (0, 1, 2)
        (0, 1, 3)
        (0, 1, 4)
        (0, 1, 5)
        (0, 2, 3)
        (0, 2, 4)
        (0, 2, 5)
        (0, 3, 4)
        (0, 3, 5)
        (0, 4, 5)
        -------------------------
        (1, 2, 3)
        (1, 2, 4)
        (1, 2, 5)
        (1, 3, 4)
        (1, 3, 5)
        (1, 4, 5)
        (2, 3, 4)
        (2, 3, 5)
        (2, 4, 5)
        (3, 4, 5)
    
'''
from itertools import combinations
import sys
input = sys.stdin.readline

# 사람 수
n = int(input())
S = [list(map(int,input().split())) for _ in range(n)]

# 능력치
stats = []
# n명 중 절반 뽑기 
for c in combinations([i for i in range(n)],n//2):
    # c에 들어간 팀원들의 능력치 합 구하기
    start = 0
    for i in c:
        for j in c:
            start += S[i][j]
    stats.append(start)

# 능력치 차이 최소 구하기
diff = float('inf')
for d in range(len(stats)//2):
    # stats[d] : 스타트 팀 능력치
    # stats[-(d+1)] : 링크 팀 능력치
    # ex) stats[0]과 stats[-1]
    diff = min(diff,abs(stats[d] - stats[-(d+1)]))
print(diff)