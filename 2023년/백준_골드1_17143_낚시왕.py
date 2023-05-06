'''
    접근법
        구현하기
    
'''
import sys
input = sys.stdin.readline

# 격자판의 크기(R,C), 상어의 수(M)
R,C,M = map(int,input().split())
# r,c,s,d,z
# (r,c)위치에 속력이 s, 방향이 d, 크기가 z인 상어
shark = [list(map(int,input().split())) for _ in range(M)]

answer = 0
for i in range(C):
    # i번째 열에 있는 상어들
    i_shark = sorted([s for s in shark if s[1]==(i+1)])
    # i번째 열에 있는 상어 중 땅에 가장 가까운 상어 잡기
    if i_shark:
        answer += i_shark[0][4]
        shark.remove(i_shark[0])
        
    # 상어 이동
    move_shark = {}
    for j in range(len(shark)):
        r,c,s,d,z = shark[j]
        k = s
        while k > 0:
            if d == 1:
                if r - k > 0:
                    r -= k
                    k = 0
                else:
                    k -= (r-1)
                    r = 1
                    d = 2
            elif d == 2:
                if r + k <= R:
                    r += k
                    k = 0
                else:
                    k -= (R-r)
                    r = R
                    d = 1
            elif d == 3:
                if c + k <= C:
                    c += k
                    k = 0
                else:
                    k -= (C-c)
                    c = C
                    d = 4
            else:
                if c - k > 0:
                    c -= k
                    k = 0
                else:
                    k -= (c-1)
                    c = 1
                    d = 3
                    
            
        # 같은 위치에 있는 상어 잡아 먹기
        if (r,c) in move_shark:
            before = move_shark[(r,c)]
            if before[4] < z:
                move_shark[(r,c)] = [r,c,s,d,z]
        else:
            move_shark[(r,c)] = [r,c,s,d,z]
            
    shark = list(move_shark.values())
    
print(answer)
